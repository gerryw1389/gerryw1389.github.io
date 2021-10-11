$apps = @(
   "4ops.terraform",
   "DavidAnson.vscode-markdownlint",
   "DotJoshJohnson.xml",
   "SolarLiner.linux-themes",
   "hashicorp.terraform",
   "jsynowiec.vscode-insertdatestring",
   "liwei.relax-eyes-theme",
   "mikey.vscode-fileheader",
   "ms-azuretools.vscode-azurefunctions",
   "ms-azuretools.vscode-azureresourcegroups",
   "ms-azuretools.vscode-logicapps",
   "ms-python.python",
   "ms-python.vscode-pylance",
   "ms-toolsai.jupyter",
   "ms-vscode-remote.remote-containers",
   "ms-vscode-remote.remote-ssh",
   "ms-vscode-remote.remote-ssh-edit",
   "ms-vscode-remote.remote-wsl",
   "ms-vscode-remote.vscode-remote-extensionpack",
   "ms-vscode.azure-account",
   "ms-vscode.powershell",
   "mushan.vscode-paste-image",
   "redhat.vscode-yaml",
   "streetsidesoftware.code-spell-checker",
   "vscode-icons-team.vscode-icons",
   "yzane.markdown-pdf",
   "yzhang.markdown-all-in-one"
)

foreach ($app in $apps)
{
   Write-Output "Installing $app"
   code --install-extension $app
}

