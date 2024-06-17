from llama_index.core.bridge.pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional

class MeaningfullMission(BaseModel):
    """ the single mission that reinforce expertise of the candidate"""
    mission_customer :str= Field(description="The name of the customer")
    mission_technology_used :str= Field(description="The list of the technology used ")
    mission_content:str= Field(description="The content of the missing")

class CriteriaDecision(BaseModel):
    """The decision made based on a single skills in german language."""

    decision: bool = Field(description="The decision made based on the skills")
    reasoning: str = Field(description="The reasoning behind the decision in german")

class CriteriaNotDecision(BaseModel):
    """The decisions made base on missing on single missing skills."""
    reasoning: str = Field(description="The reasoning behind the decision for the missing criterias")

class ResumeScreenerDecision(BaseModel):
    """The decision made by the resume screener."""

    criteria_decisions: List[CriteriaDecision] = Field(
        description="The decisions made based on the criteria in german"
    )

    supportive_missions: List[MeaningfullMission] = Field(description="The list of the missions that are validating the criterias")

    criteria_not_decisions: List[CriteriaNotDecision] = Field(
   
     description="The decisions regarding missing criterias to apply for the job in French"
    )
    
    sales_pitch:   str = Field(description="The sales pitch to apply to the position always in french")
    
    overall_reasoning: str = Field(
        description="The reasoning behind the overall decision"
    )
    overall_decision: bool = Field(
        description="The overall decision made based on the criteria"
    )
