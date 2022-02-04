#!/bin/env python
from Nemo import Production
Production.facility = "RHIC"
Production.group    = "sphenix"

from Nemo import Workflow
Workflow.shell  = "bash"
Workflow.setup  = "echo Job starts at `date`"
Workflow.finish = "echo Job ends at `date`"

from Nemo import Codeset

from beeprint import pp as pprint    # pip install beeprint

#_________________________________________________________________________________________________
#
# Build a simulation production
#
production_builder = Production.ProductionBuilder()

mc_codeset_builder = Codeset.CodesetBuilder()
mc_codeset_builder.codes.append( "macros/SimulationProduction.C : SimulationProduction.C" )  # copy to remote working directory
mc_codeset_builder.codes.append( "config/SimulationConfig.C" )                               # path will be preserved
mc_codeset_builder.codes.append( "db/" )                                                     # full directory will be copied
mc_codeset_builder.destination = "sftp::sftpblah.somewhere.gov:/scratch/nemo"                # transfer with sftp protocol

# MC workflow runs a simulation production macro...
mc_workflow_builder = Workflow.WorkflowBuilder()
mc_workflow_builder.commands = """
root.exe -q -b SimulationProduction.C
"""
mc_workflow_builder.finish = """
ls -l *.root
ls -l *.hda5
"""

production_builder.SetWorkflowBuilder( mc_workflow_builder )
production_builder.SetCodesetBuilder( mc_codeset_builder )

# Build simulation job
testMC_04 = production_builder.build("testMC_04","MC","Lib3")
pprint( testMC_04 )
testMC_04a = production_builder.build("testMC_04a","MC","Lib3")
pprint( testMC_04a )

#_________________________________________________________________________________________________
#
# Build a reconstruction production
#

# Reconstruction workflow builder
production_builder = Production.ProductionBuilder()
rc_workflow_builder = Workflow.WorkflowBuilder()
rc_workflow_builder.commands = """
root.exe -q -b ReconstructionProduction.C
root2hda5 *.root
"""
production_builder.SetWorkflowBuilder( rc_workflow_builder )

rc_codeset_builder = Codeset.CodesetBuilder()
rc_codeset_builder.codes.append( "macros/ReconstructionProduction.C : ReconstructionProduction.C" )  # copy to remote working directory
rc_codeset_builder.codes.append( "root2hda5" )
rc_codeset_builder.codes.append( "config/ReconstructionConfig.C" )                               # path will be preserved
rc_codeset_builder.codes.append( "db/" )                                                     # full directory will be copied
rc_codeset_builder.destination = "sftp::sftpblah.somewhere.gov:/scratch/nemo"                # transfer with sftp protocol

# Followed by reconstruction job
testRC_04 = production_builder.build("testRC_04","RC","Lib3",[testMC_04.unique_id,testMC_04a.unique_id])
pprint( testRC_04 )


#pp( testRC_04 )
