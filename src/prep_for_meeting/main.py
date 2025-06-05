#!/usr/bin/env python
import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from crew import PrepForMeetingCrew

def run():
    """
    Run the crew.

            "regulatory_state": "<Regulatory State>",
        "context": "<Context of the meeting>",
        "objective": "<Objective of the meeting>",
        "prior_interactions": "<Prior interactions with the participants>",

    """

    inputs = {
        "participants": [
            'Todd Loken <tjloken@gmail.com>'
        ],
        "regulatory_state": "Arkansas",
        "context": "Pharmaceutical Benefit Manager Laws in Arkansas",
        "objective": "Weekly Briefing of Laws in 2025",
        "prior_interactions": "Weekly Meeting",
    }

    PrepForMeetingCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        PrepForMeetingCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        PrepForMeetingCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        PrepForMeetingCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")