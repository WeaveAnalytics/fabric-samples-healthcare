import re
import inquirer
from needlr import auth, FabricClient
from needlr.auth import FabricInteractiveAuth, FabricServicePrincipal
from needlr.models.workspace import Workspace, WorkspaceRole, ServicePrincipal

# Get Authentication Info
questions = [inquirer.List("auth_type", message="Type of Authentication", choices=["Interactive", "Service Principal"], default="Interactive")]
answers = inquirer.prompt(questions)
if answers['auth_type'] == "Interactive":
    auth = FabricInteractiveAuth()
elif answers['auth_type'] == "Service Principal":
    questions = [
        inquirer.Text("api_id", message="Please enter your Azure Entra Application Id"),
        inquirer.Password("api_key", message="Please enter your Entra Application Secret key"),
        inquirer.Text("tenant", message="Please enter your Entra Tenant ID"),]
    answers = inquirer.prompt(questions)
    auth = FabricServicePrincipal(answers['api_id'], answers['api_key'], answers['tenant'])
else:
    print("Invalid authentication type selected.")
    exit()
fc = FabricClient(auth=auth)

exit()
# Ask for APP ID API Key and Tenant

questions = [
    inquirer.Text("api_id", message="Please enter your Azure Entra Application Id"),
    inquirer.Password("api_key", message="Please enter your Entra Application Secret key"),
    inquirer.Text("tenant", message="Please enter your Entra Tenant ID"),
]

answers = inquirer.prompt(questions)
print(answers)
auth = FabricServicePrincipal(answers['api_id'], answers['api_key'], answers['tenant'])
fc = FabricClient(auth=auth)