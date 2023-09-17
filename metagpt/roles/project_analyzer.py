from pathlib import Path
from metagpt.schema import Message
from metagpt.actions import DebugError, RunCode, WriteCode, WriteDesign, WriteTest
from metagpt.roles import Role
from metagpt.const import WORKSPACE_ROOT
import subprocess
from metagpt.utils.common import CodeParser, parse_recipient
import ast
from metagpt.logs import logger  # Import the logger

class ProjectAnalyzer(Role):
    def __init__(
        self,
        name="Alex",
        profile="ProjectAnalyzer",
        goal="Analyze the codebase to provide insights into code quality, performance, and maintainability",
        constraints="The analysis should be comprehensive, conform to code standards, and provide actionable insights",
        analysis_round_allowed=5,
    ):
        super().__init__(name, profile, goal, constraints)
        self.goal = goal
        self._init_actions(
            []  # Add any actions you want to initialize
        )
        self.analysis_round = 0
        self.analysis_round_allowed = analysis_round_allowed
        logger.info(f"Initialized {self.profile} with goal: {self.goal}")  # Log initialization

    @classmethod
    def parse_workspace(cls, system_design_msg: Message) -> str:
        if not system_design_msg.instruct_content:
            return system_design_msg.instruct_content.dict().get("Python package name")
        return CodeParser.parse_str(block="Python package name", text=system_design_msg.content)

    def get_workspace(self, return_proj_dir=True) -> Path:
        msg = self._rc.memory.get_by_action(WriteDesign)[-1]
        if not msg:
            return WORKSPACE_ROOT / "src"
        workspace = self.parse_workspace(msg)
        # project directory: workspace/{package_name}, which contains package source code folder, tests folder, resources folder, etc.
        if return_proj_dir:
            return WORKSPACE_ROOT / workspace
        # development codes directory: workspace/{package_name}/{package_name}
        return WORKSPACE_ROOT / workspace / workspace

    async def _write_analysis_report(self, message: Message) -> None:
        workspace = self.get_workspace()
        analysis_file = workspace / "analysis_report.txt"
        with open(analysis_file, "w") as f:
            f.write("Code Analysis Report\n")
            f.write("====================\n")
            f.write(message.content)
        logger.info(f"Analysis report written to {analysis_file}")  # Log report writing

    async def _run_analysis(self, msg):
        workspace = self.get_workspace()
        code_file = workspace / msg.content
        result = subprocess.run(["pylint", code_file], capture_output=True, text=True)
        analysis_result = result.stdout
        logger.debug(f"Analysis result: {analysis_result[:50]}...")  # Log analysis result (first 50 chars)

        analysis_msg = Message(
            content=analysis_result,
            role=self.profile,
            cause_by=None,
            sent_from=self.profile,
            send_to=self.profile,
        )
        self._publish_message(analysis_msg)
        await self._write_analysis_report(analysis_msg)

    async def _observe(self) -> int:
        observed_count = await super()._observe()
        logger.debug(f"Observed {observed_count} new messages")  # Log observed messages
        return observed_count

    async def _act(self) -> Message:
        if self.analysis_round > self.analysis_round_allowed:
            result_msg = Message(
                content=f"Exceeding {self.analysis_round_allowed} rounds of analysis, skip",
                role=self.profile,
                cause_by=None,
                sent_from=self.profile,
                send_to="",
            )
            logger.warning(f"Exceeded allowed rounds of analysis")  # Log warning
            return result_msg

        for msg in self._rc.news:
            if msg.cause_by == WriteCode:
                await self._run_analysis(msg)
        self.analysis_round += 1
        logger.info(f"Completed round {self.analysis_round} of analysis")  # Log completion of round

        result_msg = Message(
            content=f"Round {self.analysis_round} of analysis done",
            role=self.profile,
            cause_by=None,
            sent_from=self.profile,
            send_to="",
        )
        return result_msg
