from llama_index.core.bridge.pydantic import BaseModel, Field, ValidationError
from typing import Any, Dict, List, Optional
from enum import Enum

class Gender(str, Enum):
    """the gender of the candidate"""
    MALE = 'male'
    FEMALE = 'female'


class MeaningfullMission(BaseModel):
    """ The single mission that reinforce expertise of the candidate"""
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

    gender : Gender
    criteria_decisions: List[CriteriaDecision] = Field(
        description="The decisions made based on the criteria in german"
    )

    supportive_missions: List[MeaningfullMission] = Field(description="The list of the missions that are validating the criterias")

    criteria_not_decisions: List[CriteriaNotDecision] = Field(
   
     description="The decisions regarding missing criterias to apply for the job"
    )
    
    sales_pitch:  str = Field(description="The anonymous sales pitch to apply to the position always in french - not more than 400 characters")
    
    overall_reasoning: str = Field(
        description="The reasoning behind the overall decision"
    )
    overall_decision: bool = Field(
        description="The overall decision made based on the criteria"
    )
