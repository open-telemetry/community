# Creating a SIG-specific OTelBot GitHub App

## Step 1: Create the GitHub App

1. Navigate to the GitHub Apps creation page:
   - Go to: https://github.com/organizations/open-telemetry/settings/apps
   - Click "New GitHub App"

2. Configure the basic app settings:
   - **GitHub App name**: `otelbot <short repo name>`
     - Example: `otelbot java contrib`
   - **Homepage URL**: The repository URL where the app will be primarily used
     - Example: `https://github.com/open-telemetry/opentelemetry-java-contrib`
   - **Webhook**:
     - **Active**: UNCHECKED
   - **Repository permissions**:
     - Configure based on the specific requirements provided in the community issue
     - Commonly requested permissions include:
       - Issues: Write
       - Pull requests: Write
       - Contents: Write

3. Click "Create GitHub App"

## Step 2: Configure App Display Information

1. After creating the app, click on the app name to edit it
2. Navigate to the "Display information" section
3. **Upload a logo**:
   - Use the OpenTelemetry logo: https://avatars.githubusercontent.com/u/49998002?s=200&v=4
   - Download the image and upload it as the app logo

## Step 3: Generate and Store Private Key

1. In the app settings, scroll down to the "Private keys" section
2. Click "Generate a private key"
3. Download the generated private key file (.pem)
4. Create an organization secret:
   - Go to: https://github.com/organizations/open-telemetry/settings/secrets/actions/new
   - **Name**: `OTELBOT_<SHORT_REPO_NAME>_PRIVATE_KEY`
     - Example: `OTELBOT_JAVA_CONTRIB_PRIVATE_KEY`
   - **Secret**: Paste the contents of the downloaded .pem file
   - **Repository access**:
     - Select "Selected repositories"
     - Choose the repositories specified in the community issue
5. Delete the locally downloaded .pem file

## Step 4: Install the App

1. Return to the GitHub App settings page
2. Navigate to the "Install App" tab in the left sidebar
3. Click the "Install" button next to the OpenTelemetry organization
4. Configure installation:
   - Select "Only select repositories"
   - Choose the repositories specified in the community issue
5. Click "Install"

## Step 5: Create App ID Variable

1. Navigate to the organization variables page:
   - Go to: https://github.com/organizations/open-telemetry/settings/variables/actions
2. Click "New organization variable"
3. Configure the variable:
   - **Name**: `OTELBOT_<SHORT_REPO_NAME>_APP_ID`
     - Example: `OTELBOT_JAVA_CONTRIB_APP_ID`
   - **Value**: The App ID (found in the GitHub App settings page)
   - **Repository access**:
     - Select "Selected repositories"
     - Choose the same repositories specified in the community issue

## Step 6: Verify Installation

1. Navigate to the target repositories
2. Go to Settings → Integrations → GitHub Apps
3. Verify that the new OTelBot app appears in the installed apps list
4. Confirm that the app has the expected permissions

## Usage in GitHub Actions

Once set up, the SIG-specific OTelBot can be used in GitHub Actions workflows like this:

```yaml
- uses: actions/create-github-app-token@v1
  id: app-token
  with:
    app-id: ${{ vars.OTELBOT_JAVA_CONTRIB_APP_ID }}
    private-key: ${{ secrets.OTELBOT_JAVA_CONTRIB_PRIVATE_KEY }}

- name: Create pull request
  env:
    # Using the app token instead of GITHUB_TOKEN to trigger workflows
    GH_TOKEN: ${{ steps.app-token.outputs.token }}
  run: |
    # Your automation commands here
```

Note: you should continue to use the regular otelbot as the commit author since it is already on the EasyCLA allowlist:

```bash
git config user.name otelbot
git config user.email 197425009+otelbot@users.noreply.github.com
```

