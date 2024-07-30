# AnythingLLM Project Summary

AnythingLLM Version: 0.2.0

## Project Structure

```
├── .devcontainer
│   ├── README.md
│   └── devcontainer.json
├── .dockerignore
├── .editorconfig
├── .git
│   ├── FETCH_HEAD
│   ├── HEAD
│   ├── ORIG_HEAD
│   ├── config
│   ├── description
│   ├── hooks
│   │   ├── applypatch-msg.sample
│   │   ├── commit-msg.sample
│   │   ├── fsmonitor-watchman.sample
│   │   ├── post-update.sample
│   │   ├── pre-applypatch.sample
│   │   ├── pre-commit.sample
│   │   ├── pre-merge-commit.sample
│   │   ├── pre-push.sample
│   │   ├── pre-rebase.sample
│   │   ├── pre-receive.sample
│   │   ├── prepare-commit-msg.sample
│   │   ├── push-to-checkout.sample
│   │   └── update.sample
│   ├── index
│   ├── info
│   │   └── exclude
│   ├── logs
│   │   ├── HEAD
│   │   └── refs
│   │   │   ├── heads
│   │   │   │   ├── ayang
│   │   │   │   │   └── rag-platform
│   │   │   │   └── master
│   │   │   └── remotes
│   │   │   │   └── origin
│   │   │   │   │   └── HEAD
│   ├── objects
│   │   ├── info
│   │   └── pack
│   │   │   ├── pack-827c044d3790dee34d9dd51953c0ad9fe90eee7f.idx
│   │   │   └── pack-827c044d3790dee34d9dd51953c0ad9fe90eee7f.pack
│   ├── packed-refs
│   └── refs
│   │   ├── heads
│   │   │   ├── ayang
│   │   │   │   └── rag-platform
│   │   │   └── master
│   │   ├── remotes
│   │   │   └── origin
│   │   │   │   └── HEAD
│   │   └── tags
├── .gitattributes
├── .github
│   ├── FUNDING.yml
│   ├── ISSUE_TEMPLATE
│   │   ├── 01_bug.yml
│   │   ├── 02_feature.yml
│   │   ├── 03_documentation.yml
│   │   └── config.yml
│   └── workflows
│   │   ├── build-and-push-image.yaml
│   │   └── check-translations.yaml
├── .gitignore
├── .hadolint.yaml
├── .nvmrc
├── .prettierignore
├── .prettierrc
├── .vscode
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
├── BARE_METAL.md
├── LICENSE
├── README.md
├── SECURITY.md
├── anythingllm_summary.md
├── cloud-deployments
│   ├── aws
│   │   └── cloudformation
│   │   │   ├── DEPLOY.md
│   │   │   ├── aws_https_instructions.md
│   │   │   └── cloudformation_create_anythingllm.json
│   ├── digitalocean
│   │   └── terraform
│   │   │   ├── DEPLOY.md
│   │   │   ├── main.tf
│   │   │   ├── outputs.tf
│   │   │   └── user_data.tp1
│   ├── gcp
│   │   └── deployment
│   │   │   ├── DEPLOY.md
│   │   │   └── gcp_deploy_anything_llm.yaml
│   └── k8
│   │   └── manifest.yaml
├── collector
│   ├── .env.example
│   ├── .gitignore
│   ├── .nvmrc
│   ├── extensions
│   │   ├── index.js
│   │   └── resync
│   │   │   └── index.js
│   ├── hotdir
│   │   └── __HOTDIR__.md
│   ├── index.js
│   ├── middleware
│   │   ├── setDataSigner.js
│   │   └── verifyIntegrity.js
│   ├── nodemon.json
│   ├── package.json
│   ├── processLink
│   │   ├── convert
│   │   │   └── generic.js
│   │   └── index.js
│   ├── processRawText
│   │   └── index.js
│   ├── processSingleFile
│   │   ├── convert
│   │   │   ├── asAudio.js
│   │   │   ├── asDocx.js
│   │   │   ├── asEPub.js
│   │   │   ├── asMbox.js
│   │   │   ├── asOfficeMime.js
│   │   │   ├── asPDF
│   │   │   │   ├── PDFLoader
│   │   │   │   │   └── index.js
│   │   │   │   └── index.js
│   │   │   └── asTxt.js
│   │   └── index.js
│   ├── storage
│   │   ├── .gitignore
│   │   └── tmp
│   │   │   └── .placeholder
│   ├── utils
│   │   ├── EncryptionWorker
│   │   │   └── index.js
│   │   ├── WhisperProviders
│   │   │   ├── OpenAiWhisper.js
│   │   │   └── localWhisper.js
│   │   ├── comKey
│   │   │   └── index.js
│   │   ├── constants.js
│   │   ├── extensions
│   │   │   ├── Confluence
│   │   │   │   ├── ConfluenceLoader
│   │   │   │   │   └── index.js
│   │   │   │   └── index.js
│   │   │   ├── GithubRepo
│   │   │   │   ├── RepoLoader
│   │   │   │   │   └── index.js
│   │   │   │   └── index.js
│   │   │   ├── WebsiteDepth
│   │   │   │   └── index.js
│   │   │   └── YoutubeTranscript
│   │   │   │   ├── YoutubeLoader
│   │   │   │   │   ├── index.js
│   │   │   │   │   └── youtube-transcript.js
│   │   │   │   └── index.js
│   │   ├── files
│   │   │   ├── index.js
│   │   │   └── mime.js
│   │   ├── http
│   │   │   └── index.js
│   │   ├── logger
│   │   │   └── index.js
│   │   ├── tokenizer
│   │   │   └── index.js
│   │   └── url
│   │   │   └── index.js
│   └── yarn.lock
├── concise-anythingllm-summary.py
├── docker
│   ├── .env.example
│   ├── Dockerfile
│   ├── HOW_TO_USE_DOCKER.md
│   ├── docker-compose.yml
│   ├── docker-entrypoint.sh
│   ├── docker-healthcheck.sh
│   └── vex
│   │   └── CVE-2024-37890.vex.json
├── embed
│   ├── .gitignore
│   ├── README.md
│   ├── index.html
│   ├── jsconfig.json
│   ├── package.json
│   ├── postcss.config.js
│   ├── scripts
│   │   └── updateHljs.mjs
│   ├── src
│   │   ├── App.jsx
│   │   ├── assets
│   │   │   ├── anything-llm-dark.png
│   │   │   └── anything-llm-icon.svg
│   │   ├── components
│   │   │   ├── ChatWindow
│   │   │   │   ├── ChatContainer
│   │   │   │   │   ├── ChatHistory
│   │   │   │   │   │   ├── HistoricalMessage
│   │   │   │   │   │   │   ├── Actions
│   │   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   ├── PromptReply
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── PromptInput
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── Header
│   │   │   │   │   └── index.jsx
│   │   │   │   └── index.jsx
│   │   │   ├── Head.jsx
│   │   │   ├── OpenButton
│   │   │   │   └── index.jsx
│   │   │   ├── ResetChat
│   │   │   │   └── index.jsx
│   │   │   ├── SessionId
│   │   │   │   └── index.jsx
│   │   │   └── Sponsor
│   │   │   │   └── index.jsx
│   │   ├── hooks
│   │   │   ├── chat
│   │   │   │   └── useChatHistory.js
│   │   │   ├── useOpen.js
│   │   │   ├── useScriptAttributes.js
│   │   │   └── useSessionId.js
│   │   ├── index.css
│   │   ├── main.jsx
│   │   ├── models
│   │   │   └── chatService.js
│   │   └── utils
│   │   │   ├── chat
│   │   │   │   ├── hljs.js
│   │   │   │   ├── index.js
│   │   │   │   └── markdown.js
│   │   │   ├── constants.js
│   │   │   └── date.js
│   ├── tailwind.config.js
│   ├── vite.config.js
│   └── yarn.lock
├── eslint.config.js
├── frontend
│   ├── .env.example
│   ├── .gitignore
│   ├── .nvmrc
│   ├── index.html
│   ├── jsconfig.json
│   ├── package.json
│   ├── postcss.config.js
│   ├── public
│   │   ├── anything-llm-dark.png
│   │   ├── anything-llm-light.png
│   │   ├── embed
│   │   │   ├── anythingllm-chat-widget.min.css
│   │   │   └── anythingllm-chat-widget.min.js
│   │   ├── favicon.ico
│   │   ├── favicon.png
│   │   ├── fonts
│   │   │   └── PlusJakartaSans.ttf
│   │   └── robots.txt
│   ├── scripts
│   │   └── postbuild.js
│   ├── src
│   │   ├── App.jsx
│   │   ├── AuthContext.jsx
│   │   ├── LogoContext.jsx
│   │   ├── PfpContext.jsx
│   │   ├── components
│   │   │   ├── ChangeWarning
│   │   │   │   └── index.jsx
│   │   │   ├── ChatBubble
│   │   │   │   └── index.jsx
│   │   │   ├── ContextualSaveBar
│   │   │   │   └── index.jsx
│   │   │   ├── DataConnectorOption
│   │   │   │   ├── index.jsx
│   │   │   │   └── media
│   │   │   │   │   ├── confluence.jpeg
│   │   │   │   │   ├── github.svg
│   │   │   │   │   ├── index.js
│   │   │   │   │   ├── link.svg
│   │   │   │   │   └── youtube.svg
│   │   │   ├── DefaultChat
│   │   │   │   └── index.jsx
│   │   │   ├── EditingChatBubble
│   │   │   │   └── index.jsx
│   │   │   ├── EmbeddingSelection
│   │   │   │   ├── AzureAiOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── CohereOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── EmbedderItem
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── GenericOpenAiOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── LMStudioOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── LiteLLMOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── LocalAiOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── NativeEmbeddingOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── OllamaOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── OpenAiOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   └── VoyageAiOptions
│   │   │   │   │   └── index.jsx
│   │   │   ├── Footer
│   │   │   │   └── index.jsx
│   │   │   ├── LLMSelection
│   │   │   │   ├── AnthropicAiOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── AzureAiOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── CohereAiOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── GeminiLLMOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── GenericOpenAiOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── GroqAiOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── HuggingFaceOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── KoboldCPPOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── LLMItem
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── LLMProviderOption
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── LMStudioOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── LiteLLMOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── LocalAiOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── MistralOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── NativeLLMOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── OllamaLLMOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── OpenAiOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── OpenRouterOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── PerplexityOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── TextGenWebUIOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   └── TogetherAiOptions
│   │   │   │   │   └── index.jsx
│   │   │   ├── ModalWrapper
│   │   │   │   └── index.jsx
│   │   │   ├── Modals
│   │   │   │   ├── DisplayRecoveryCodeModal
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── ManageWorkspace
│   │   │   │   │   ├── DataConnectors
│   │   │   │   │   │   ├── ConnectorOption
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   ├── Connectors
│   │   │   │   │   │   │   ├── Confluence
│   │   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   │   ├── Github
│   │   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   │   ├── WebsiteDepth
│   │   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   │   └── Youtube
│   │   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── Documents
│   │   │   │   │   │   ├── Directory
│   │   │   │   │   │   │   ├── FileRow
│   │   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   │   ├── FolderRow
│   │   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   │   ├── FolderSelectionPopup
│   │   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   │   ├── MoveToFolderIcon.jsx
│   │   │   │   │   │   │   ├── NewFolderModal
│   │   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   │   ├── index.jsx
│   │   │   │   │   │   │   └── utils.js
│   │   │   │   │   │   ├── UploadFile
│   │   │   │   │   │   │   ├── FileUploadProgress
│   │   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   ├── WorkspaceDirectory
│   │   │   │   │   │   │   ├── WorkspaceFileRow
│   │   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── NewWorkspace.jsx
│   │   │   │   └── Password
│   │   │   │   │   ├── MultiUserAuth.jsx
│   │   │   │   │   ├── SingleUserAuth.jsx
│   │   │   │   │   └── index.jsx
│   │   │   ├── Preloader.jsx
│   │   │   ├── PrivateRoute
│   │   │   │   └── index.jsx
│   │   │   ├── SettingsButton
│   │   │   │   └── index.jsx
│   │   │   ├── SettingsSidebar
│   │   │   │   ├── MenuOption
│   │   │   │   │   └── index.jsx
│   │   │   │   └── index.jsx
│   │   │   ├── Sidebar
│   │   │   │   ├── ActiveWorkspaces
│   │   │   │   │   ├── ThreadContainer
│   │   │   │   │   │   ├── ThreadItem
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   └── index.jsx
│   │   │   ├── SpeechToText
│   │   │   │   └── BrowserNative
│   │   │   │   │   └── index.jsx
│   │   │   ├── TextToSpeech
│   │   │   │   ├── BrowserNative
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── ElevenLabsOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   └── OpenAiOptions
│   │   │   │   │   └── index.jsx
│   │   │   ├── TranscriptionSelection
│   │   │   │   ├── NativeTranscriptionOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   └── OpenAiOptions
│   │   │   │   │   └── index.jsx
│   │   │   ├── UserIcon
│   │   │   │   ├── index.jsx
│   │   │   │   └── workspace.png
│   │   │   ├── UserMenu
│   │   │   │   ├── AccountModal
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── UserButton
│   │   │   │   │   └── index.jsx
│   │   │   │   └── index.jsx
│   │   │   ├── VectorDBSelection
│   │   │   │   ├── AstraDBOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── ChromaDBOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── LanceDBOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── MilvusDBOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── PineconeDBOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── QDrantDBOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── VectorDBItem
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── WeaviateDBOptions
│   │   │   │   │   └── index.jsx
│   │   │   │   └── ZillizCloudOptions
│   │   │   │   │   └── index.jsx
│   │   │   ├── WorkspaceChat
│   │   │   │   ├── ChatContainer
│   │   │   │   │   ├── ChatHistory
│   │   │   │   │   │   ├── Chartable
│   │   │   │   │   │   │   ├── CustomCell.jsx
│   │   │   │   │   │   │   ├── CustomTooltip.jsx
│   │   │   │   │   │   │   ├── chart-utils.js
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   ├── Citation
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   ├── HistoricalMessage
│   │   │   │   │   │   │   ├── Actions
│   │   │   │   │   │   │   │   ├── ActionMenu
│   │   │   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   │   │   ├── DeleteMessage
│   │   │   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   │   │   ├── EditMessage
│   │   │   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   │   │   ├── TTSButton
│   │   │   │   │   │   │   │   │   ├── asyncTts.jsx
│   │   │   │   │   │   │   │   │   ├── index.jsx
│   │   │   │   │   │   │   │   │   └── native.jsx
│   │   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   ├── PromptReply
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── PromptInput
│   │   │   │   │   │   ├── AgentMenu
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   ├── SlashCommands
│   │   │   │   │   │   │   ├── SlashPresets
│   │   │   │   │   │   │   │   ├── AddPresetModal.jsx
│   │   │   │   │   │   │   │   ├── EditPresetModal.jsx
│   │   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   │   ├── endAgentSession.jsx
│   │   │   │   │   │   │   ├── icons
│   │   │   │   │   │   │   │   └── slash-commands-icon.svg
│   │   │   │   │   │   │   ├── index.jsx
│   │   │   │   │   │   │   └── reset.jsx
│   │   │   │   │   │   ├── SpeechToText
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   ├── StopGenerationButton
│   │   │   │   │   │   │   ├── index.jsx
│   │   │   │   │   │   │   └── stop.svg
│   │   │   │   │   │   ├── TextSizeMenu
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── LoadingChat
│   │   │   │   │   └── index.jsx
│   │   │   │   └── index.jsx
│   │   │   └── lib
│   │   │   │   └── CTAButton
│   │   │   │   │   └── index.jsx
│   │   ├── hooks
│   │   │   ├── useCopyText.js
│   │   │   ├── useGetProvidersModels.js
│   │   │   ├── useLanguageOptions.js
│   │   │   ├── useLoginMode.js
│   │   │   ├── useLogo.js
│   │   │   ├── useModal.js
│   │   │   ├── usePfp.js
│   │   │   ├── usePrefersDarkMode.js
│   │   │   ├── useProviderEndpointAutoDiscovery.js
│   │   │   ├── useQuery.js
│   │   │   └── useUser.js
│   │   ├── i18n.js
│   │   ├── index.css
│   │   ├── locales
│   │   │   ├── en
│   │   │   │   └── common.js
│   │   │   ├── es
│   │   │   │   └── common.js
│   │   │   ├── fr
│   │   │   │   └── common.js
│   │   │   ├── ko
│   │   │   │   └── common.js
│   │   │   ├── resources.js
│   │   │   ├── ru
│   │   │   │   └── common.js
│   │   │   ├── verifyTranslations.mjs
│   │   │   └── zh
│   │   │   │   └── common.js
│   │   ├── main.jsx
│   │   ├── media
│   │   │   ├── agents
│   │   │   │   ├── generate-charts.png
│   │   │   │   ├── generate-save-files.png
│   │   │   │   ├── rag-memory.png
│   │   │   │   ├── scrape-websites.png
│   │   │   │   ├── sql-agent.png
│   │   │   │   └── view-summarize.png
│   │   │   ├── dataConnectors
│   │   │   │   └── confluence.png
│   │   │   ├── embeddingprovider
│   │   │   │   └── voyageai.png
│   │   │   ├── illustrations
│   │   │   │   ├── create-workspace.png
│   │   │   │   ├── login-illustration.svg
│   │   │   │   └── login-logo.svg
│   │   │   ├── llmprovider
│   │   │   │   ├── anthropic.png
│   │   │   │   ├── azure.png
│   │   │   │   ├── cohere.png
│   │   │   │   ├── gemini.png
│   │   │   │   ├── generic-openai.png
│   │   │   │   ├── groq.png
│   │   │   │   ├── huggingface.png
│   │   │   │   ├── koboldcpp.png
│   │   │   │   ├── litellm.png
│   │   │   │   ├── lmstudio.png
│   │   │   │   ├── localai.png
│   │   │   │   ├── mistral.jpeg
│   │   │   │   ├── ollama.png
│   │   │   │   ├── openai.png
│   │   │   │   ├── openrouter.jpeg
│   │   │   │   ├── perplexity.png
│   │   │   │   ├── text-generation-webui.png
│   │   │   │   └── togetherai.png
│   │   │   ├── logo
│   │   │   │   ├── anything-llm-icon.png
│   │   │   │   ├── anything-llm-old.png
│   │   │   │   └── anything-llm.png
│   │   │   ├── ttsproviders
│   │   │   │   └── elevenlabs.png
│   │   │   └── vectordbs
│   │   │   │   ├── astraDB.png
│   │   │   │   ├── chroma.png
│   │   │   │   ├── lancedb.png
│   │   │   │   ├── milvus.png
│   │   │   │   ├── pinecone.png
│   │   │   │   ├── qdrant.png
│   │   │   │   ├── weaviate.png
│   │   │   │   └── zilliz.png
│   │   ├── models
│   │   │   ├── admin.js
│   │   │   ├── dataConnector.js
│   │   │   ├── document.js
│   │   │   ├── embed.js
│   │   │   ├── experimental
│   │   │   │   └── liveSync.js
│   │   │   ├── invite.js
│   │   │   ├── system.js
│   │   │   ├── workspace.js
│   │   │   └── workspaceThread.js
│   │   ├── pages
│   │   │   ├── 404.jsx
│   │   │   ├── Admin
│   │   │   │   ├── Agents
│   │   │   │   │   ├── Badges
│   │   │   │   │   │   └── default.jsx
│   │   │   │   │   ├── DefaultSkillPanel
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── GenericSkillPanel
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── SQLConnectorSelection
│   │   │   │   │   │   ├── DBConnection.jsx
│   │   │   │   │   │   ├── NewConnectionModal.jsx
│   │   │   │   │   │   ├── icons
│   │   │   │   │   │   │   ├── mssql.png
│   │   │   │   │   │   │   ├── mysql.png
│   │   │   │   │   │   │   └── postgresql.png
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── WebSearchSelection
│   │   │   │   │   │   ├── SearchProviderItem
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   ├── SearchProviderOptions
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   ├── icons
│   │   │   │   │   │   │   ├── bing.png
│   │   │   │   │   │   │   ├── google.png
│   │   │   │   │   │   │   ├── searxng.png
│   │   │   │   │   │   │   ├── serper.png
│   │   │   │   │   │   │   └── serply.png
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── index.jsx
│   │   │   │   │   └── skills.js
│   │   │   │   ├── ExperimentalFeatures
│   │   │   │   │   ├── Features
│   │   │   │   │   │   └── LiveSync
│   │   │   │   │   │   │   ├── manage
│   │   │   │   │   │   │   │   ├── DocumentSyncQueueRow
│   │   │   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   │   └── toggle.jsx
│   │   │   │   │   ├── features.js
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── Invitations
│   │   │   │   │   ├── InviteRow
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── NewInviteModal
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── Logging
│   │   │   │   │   ├── LogRow
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── System
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── Users
│   │   │   │   │   ├── NewUserModal
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── UserRow
│   │   │   │   │   │   ├── EditUserModal
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   └── Workspaces
│   │   │   │   │   ├── NewWorkspaceModal
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── WorkspaceRow
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   ├── GeneralSettings
│   │   │   │   ├── ApiKeys
│   │   │   │   │   ├── ApiKeyRow
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── NewApiKeyModal
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── Appearance
│   │   │   │   │   ├── CustomAppName
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── CustomLogo
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── CustomMessages
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── CustomSiteSettings
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── FooterCustomization
│   │   │   │   │   │   ├── NewIconForm
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── LanguagePreference
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── SupportEmail
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── AudioPreference
│   │   │   │   │   ├── index.jsx
│   │   │   │   │   ├── stt.jsx
│   │   │   │   │   └── tts.jsx
│   │   │   │   ├── Chats
│   │   │   │   │   ├── ChatRow
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── EmbedChats
│   │   │   │   │   ├── ChatRow
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── EmbedConfigs
│   │   │   │   │   ├── EmbedRow
│   │   │   │   │   │   ├── CodeSnippetModal
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   ├── EditEmbedModal
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── NewEmbedModal
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── EmbeddingPreference
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── EmbeddingTextSplitterPreference
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── LLMPreference
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── PrivacyAndData
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── Security
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── TranscriptionPreference
│   │   │   │   │   └── index.jsx
│   │   │   │   └── VectorDatabase
│   │   │   │   │   └── index.jsx
│   │   │   ├── Invite
│   │   │   │   ├── NewUserModal
│   │   │   │   │   └── index.jsx
│   │   │   │   └── index.jsx
│   │   │   ├── Login
│   │   │   │   └── index.jsx
│   │   │   ├── Main
│   │   │   │   └── index.jsx
│   │   │   ├── OnboardingFlow
│   │   │   │   ├── Steps
│   │   │   │   │   ├── CreateWorkspace
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── DataHandling
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── Home
│   │   │   │   │   │   ├── index.jsx
│   │   │   │   │   │   ├── l_group.png
│   │   │   │   │   │   └── r_group.png
│   │   │   │   │   ├── LLMPreference
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── Survey
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── UserSetup
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   └── index.jsx
│   │   │   ├── WorkspaceChat
│   │   │   │   └── index.jsx
│   │   │   └── WorkspaceSettings
│   │   │   │   ├── AgentConfig
│   │   │   │   │   ├── AgentLLMSelection
│   │   │   │   │   │   ├── AgentLLMItem
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── AgentModelSelection
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── ChatSettings
│   │   │   │   │   ├── ChatHistorySettings
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── ChatModeSelection
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── ChatPromptSettings
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── ChatQueryRefusalResponse
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── ChatTemperatureSettings
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── WorkspaceLLMSelection
│   │   │   │   │   │   ├── ChatModelSelection
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   ├── WorkspaceLLMItem
│   │   │   │   │   │   │   └── index.jsx
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── GeneralAppearance
│   │   │   │   │   ├── DeleteWorkspace
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── SuggestedChatMessages
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── WorkspaceName
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── WorkspacePfp
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── Members
│   │   │   │   │   ├── AddMemberModal
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── WorkspaceMemberRow
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── VectorDatabase
│   │   │   │   │   ├── DocumentSimilarityThreshold
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── MaxContextSnippets
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── ResetDatabase
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── VectorCount
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── VectorDBIdentifier
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   └── index.jsx
│   │   └── utils
│   │   │   ├── chat
│   │   │   │   ├── agent.js
│   │   │   │   ├── index.js
│   │   │   │   └── markdown.js
│   │   │   ├── constants.js
│   │   │   ├── directories.js
│   │   │   ├── numbers.js
│   │   │   ├── paths.js
│   │   │   ├── request.js
│   │   │   ├── session.js
│   │   │   ├── toast.js
│   │   │   └── types.js
│   ├── tailwind.config.js
│   ├── vite.config.js
│   └── yarn.lock
├── images
│   ├── LLMproviders
│   │   ├── localai-embedding.png
│   │   └── localai-setup.png
│   ├── choices.png
│   ├── deployBtns
│   │   ├── aws.png
│   │   └── docker.png
│   ├── gcp-project-bar.png
│   ├── promo.png
│   ├── screenshots
│   │   ├── cf_outputs.png
│   │   ├── create_stack.png
│   │   └── upload.png
│   ├── wordmark.png
│   └── youtube.png
├── locales
│   ├── README.ja-JP.md
│   └── README.zh-CN.md
├── package.json
├── pull_request_template.md
└── server
│   ├── .env.example
│   ├── .flowconfig
│   ├── .gitignore
│   ├── .nvmrc
│   ├── endpoints
│   │   ├── admin.js
│   │   ├── agentWebsocket.js
│   │   ├── api
│   │   │   ├── admin
│   │   │   │   └── index.js
│   │   │   ├── auth
│   │   │   │   └── index.js
│   │   │   ├── document
│   │   │   │   └── index.js
│   │   │   ├── index.js
│   │   │   ├── openai
│   │   │   │   ├── compatibility-test-script.cjs
│   │   │   │   └── index.js
│   │   │   ├── system
│   │   │   │   └── index.js
│   │   │   ├── userManagement
│   │   │   │   └── index.js
│   │   │   ├── workspace
│   │   │   │   └── index.js
│   │   │   └── workspaceThread
│   │   │   │   └── index.js
│   │   ├── chat.js
│   │   ├── document.js
│   │   ├── embed
│   │   │   └── index.js
│   │   ├── embedManagement.js
│   │   ├── experimental
│   │   │   ├── index.js
│   │   │   └── liveSync.js
│   │   ├── extensions
│   │   │   └── index.js
│   │   ├── invite.js
│   │   ├── system.js
│   │   ├── utils.js
│   │   ├── workspaceThreads.js
│   │   └── workspaces.js
│   ├── index.js
│   ├── jobs
│   │   ├── helpers
│   │   │   └── index.js
│   │   └── sync-watched-documents.js
│   ├── jsconfig.json
│   ├── models
│   │   ├── apiKeys.js
│   │   ├── cacheData.js
│   │   ├── documentSyncQueue.js
│   │   ├── documentSyncRun.js
│   │   ├── documents.js
│   │   ├── embedChats.js
│   │   ├── embedConfig.js
│   │   ├── eventLogs.js
│   │   ├── invite.js
│   │   ├── passwordRecovery.js
│   │   ├── slashCommandsPresets.js
│   │   ├── systemSettings.js
│   │   ├── telemetry.js
│   │   ├── user.js
│   │   ├── vectors.js
│   │   ├── welcomeMessages.js
│   │   ├── workspace.js
│   │   ├── workspaceAgentInvocation.js
│   │   ├── workspaceChats.js
│   │   ├── workspaceThread.js
│   │   ├── workspaceUsers.js
│   │   └── workspacesSuggestedMessages.js
│   ├── nodemon.json
│   ├── package.json
│   ├── prisma
│   │   ├── migrations
│   │   │   ├── 20230921191814_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20231101001441_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20231101195421_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20231129012019_add
│   │   │   │   └── migration.sql
│   │   │   ├── 20240113013409_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20240118201333_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20240202002020_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20240206181106_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20240206211916_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20240208224848_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20240210004405_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20240216214639_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20240219211018_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20240301002308_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20240326231053_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20240405015034_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20240412183346_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20240425004220_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20240430230707_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20240510032311_init
│   │   │   │   └── migration.sql
│   │   │   ├── 20240618224346_init
│   │   │   │   └── migration.sql
│   │   │   └── migration_lock.toml
│   │   ├── schema.prisma
│   │   └── seed.js
│   ├── storage
│   │   ├── README.md
│   │   ├── assets
│   │   │   └── anything-llm.png
│   │   ├── documents
│   │   │   └── DOCUMENTS.md
│   │   ├── models
│   │   │   ├── .gitignore
│   │   │   ├── README.md
│   │   │   └── downloaded
│   │   │   │   └── .placeholder
│   │   └── vector-cache
│   │   │   └── VECTOR_CACHE.md
│   ├── swagger
│   │   ├── dark-swagger.css
│   │   ├── index.css
│   │   ├── index.js
│   │   ├── init.js
│   │   ├── openapi.json
│   │   └── utils.js
│   ├── utils
│   │   ├── AiProviders
│   │   │   ├── anthropic
│   │   │   │   └── index.js
│   │   │   ├── azureOpenAi
│   │   │   │   └── index.js
│   │   │   ├── cohere
│   │   │   │   └── index.js
│   │   │   ├── gemini
│   │   │   │   └── index.js
│   │   │   ├── genericOpenAi
│   │   │   │   └── index.js
│   │   │   ├── groq
│   │   │   │   └── index.js
│   │   │   ├── huggingface
│   │   │   │   └── index.js
│   │   │   ├── koboldCPP
│   │   │   │   └── index.js
│   │   │   ├── liteLLM
│   │   │   │   └── index.js
│   │   │   ├── lmStudio
│   │   │   │   └── index.js
│   │   │   ├── localAi
│   │   │   │   └── index.js
│   │   │   ├── mistral
│   │   │   │   └── index.js
│   │   │   ├── native
│   │   │   │   └── index.js
│   │   │   ├── ollama
│   │   │   │   ├── README.md
│   │   │   │   └── index.js
│   │   │   ├── openAi
│   │   │   │   └── index.js
│   │   │   ├── openRouter
│   │   │   │   └── index.js
│   │   │   ├── perplexity
│   │   │   │   ├── index.js
│   │   │   │   ├── models.js
│   │   │   │   └── scripts
│   │   │   │   │   ├── .gitignore
│   │   │   │   │   ├── chat_models.txt
│   │   │   │   │   └── parse.mjs
│   │   │   ├── textGenWebUI
│   │   │   │   └── index.js
│   │   │   └── togetherAi
│   │   │   │   ├── index.js
│   │   │   │   ├── models.js
│   │   │   │   └── scripts
│   │   │   │   │   ├── .gitignore
│   │   │   │   │   ├── chat_models.txt
│   │   │   │   │   └── parse.mjs
│   │   ├── BackgroundWorkers
│   │   │   └── index.js
│   │   ├── DocumentManager
│   │   │   └── index.js
│   │   ├── EmbeddingEngines
│   │   │   ├── azureOpenAi
│   │   │   │   └── index.js
│   │   │   ├── cohere
│   │   │   │   └── index.js
│   │   │   ├── genericOpenAi
│   │   │   │   └── index.js
│   │   │   ├── liteLLM
│   │   │   │   └── index.js
│   │   │   ├── lmstudio
│   │   │   │   └── index.js
│   │   │   ├── localAi
│   │   │   │   └── index.js
│   │   │   ├── native
│   │   │   │   └── index.js
│   │   │   ├── ollama
│   │   │   │   └── index.js
│   │   │   ├── openAi
│   │   │   │   └── index.js
│   │   │   └── voyageAi
│   │   │   │   └── index.js
│   │   ├── EncryptionManager
│   │   │   └── index.js
│   │   ├── PasswordRecovery
│   │   │   └── index.js
│   │   ├── TextSplitter
│   │   │   └── index.js
│   │   ├── TextToSpeech
│   │   │   ├── elevenLabs
│   │   │   │   └── index.js
│   │   │   ├── index.js
│   │   │   └── openAi
│   │   │   │   └── index.js
│   │   ├── agents
│   │   │   ├── aibitat
│   │   │   │   ├── error.js
│   │   │   │   ├── example
│   │   │   │   │   ├── .gitignore
│   │   │   │   │   ├── beginner-chat.js
│   │   │   │   │   ├── blog-post-coding.js
│   │   │   │   │   └── websocket
│   │   │   │   │   │   ├── index.html
│   │   │   │   │   │   ├── websock-branding-collab.js
│   │   │   │   │   │   └── websock-multi-turn-chat.js
│   │   │   │   ├── index.js
│   │   │   │   ├── plugins
│   │   │   │   │   ├── chat-history.js
│   │   │   │   │   ├── cli.js
│   │   │   │   │   ├── file-history.js
│   │   │   │   │   ├── index.js
│   │   │   │   │   ├── memory.js
│   │   │   │   │   ├── rechart.js
│   │   │   │   │   ├── save-file-browser.js
│   │   │   │   │   ├── sql-agent
│   │   │   │   │   │   ├── SQLConnectors
│   │   │   │   │   │   │   ├── MSSQL.js
│   │   │   │   │   │   │   ├── MySQL.js
│   │   │   │   │   │   │   ├── Postgresql.js
│   │   │   │   │   │   │   └── index.js
│   │   │   │   │   │   ├── get-table-schema.js
│   │   │   │   │   │   ├── index.js
│   │   │   │   │   │   ├── list-database.js
│   │   │   │   │   │   ├── list-table.js
│   │   │   │   │   │   └── query.js
│   │   │   │   │   ├── summarize.js
│   │   │   │   │   ├── web-browsing.js
│   │   │   │   │   ├── web-scraping.js
│   │   │   │   │   └── websocket.js
│   │   │   │   ├── providers
│   │   │   │   │   ├── ai-provider.js
│   │   │   │   │   ├── anthropic.js
│   │   │   │   │   ├── azure.js
│   │   │   │   │   ├── genericOpenAi.js
│   │   │   │   │   ├── groq.js
│   │   │   │   │   ├── helpers
│   │   │   │   │   │   ├── classes.js
│   │   │   │   │   │   └── untooled.js
│   │   │   │   │   ├── index.js
│   │   │   │   │   ├── koboldcpp.js
│   │   │   │   │   ├── lmstudio.js
│   │   │   │   │   ├── localai.js
│   │   │   │   │   ├── mistral.js
│   │   │   │   │   ├── ollama.js
│   │   │   │   │   ├── openai.js
│   │   │   │   │   ├── openrouter.js
│   │   │   │   │   ├── perplexity.js
│   │   │   │   │   ├── textgenwebui.js
│   │   │   │   │   └── togetherai.js
│   │   │   │   └── utils
│   │   │   │   │   ├── dedupe.js
│   │   │   │   │   └── summarize.js
│   │   │   ├── defaults.js
│   │   │   └── index.js
│   │   ├── boot
│   │   │   ├── MetaGenerator.js
│   │   │   └── index.js
│   │   ├── chats
│   │   │   ├── agents.js
│   │   │   ├── commands
│   │   │   │   └── reset.js
│   │   │   ├── embed.js
│   │   │   ├── index.js
│   │   │   ├── openaiCompatible.js
│   │   │   └── stream.js
│   │   ├── collectorApi
│   │   │   └── index.js
│   │   ├── comKey
│   │   │   └── index.js
│   │   ├── database
│   │   │   └── index.js
│   │   ├── files
│   │   │   ├── index.js
│   │   │   ├── logo.js
│   │   │   ├── multer.js
│   │   │   ├── pfp.js
│   │   │   └── purgeDocument.js
│   │   ├── helpers
│   │   │   ├── admin
│   │   │   │   └── index.js
│   │   │   ├── camelcase.js
│   │   │   ├── chat
│   │   │   │   ├── convertTo.js
│   │   │   │   ├── index.js
│   │   │   │   └── responses.js
│   │   │   ├── customModels.js
│   │   │   ├── index.js
│   │   │   ├── portAvailabilityChecker.js
│   │   │   ├── tiktoken.js
│   │   │   └── updateENV.js
│   │   ├── http
│   │   │   └── index.js
│   │   ├── logger
│   │   │   └── index.js
│   │   ├── middleware
│   │   │   ├── embedMiddleware.js
│   │   │   ├── featureFlagEnabled.js
│   │   │   ├── multiUserProtected.js
│   │   │   ├── validApiKey.js
│   │   │   ├── validWorkspace.js
│   │   │   └── validatedRequest.js
│   │   ├── prisma
│   │   │   ├── PRISMA.md
│   │   │   ├── index.js
│   │   │   └── migrateFromSqlite.js
│   │   ├── telemetry
│   │   │   └── index.js
│   │   └── vectorDbProviders
│   │   │   ├── astra
│   │   │   │   ├── ASTRA_SETUP.md
│   │   │   │   └── index.js
│   │   │   ├── chroma
│   │   │   │   ├── CHROMA_SETUP.md
│   │   │   │   └── index.js
│   │   │   ├── lance
│   │   │   │   └── index.js
│   │   │   ├── milvus
│   │   │   │   ├── MILVUS_SETUP.md
│   │   │   │   └── index.js
│   │   │   ├── pinecone
│   │   │   │   ├── PINECONE_SETUP.md
│   │   │   │   └── index.js
│   │   │   ├── qdrant
│   │   │   │   ├── QDRANT_SETUP.md
│   │   │   │   └── index.js
│   │   │   ├── weaviate
│   │   │   │   ├── WEAVIATE_SETUP.md
│   │   │   │   └── index.js
│   │   │   └── zilliz
│   │   │   │   └── index.js
│   └── yarn.lock
```

README Summary:
Section: Product Overview
   AnythingLLM is a full-stack application where you can use commercial off-the-shelf LLMs or popular open source LLMs and vectorDB solutions to build a private ChatGPT with no compromises that you can ...
Section: Supported LLMs, Embedder Models, Speech models, and Vector Databases
   **Language Learning Models:**  - [Any open-source llama.cpp compatible model](/server/storage/models/README.md#text-generation-llm-selection) - [OpenAI](https://openai.com) - [OpenAI (Generic)](https...
Section: Technical Overview
   This monorepo consists of three main sections:  - `frontend`: A viteJS + React frontend that you can run to easily create and manage all your content the LLM can use. - `server`: A NodeJS express ser...
Section: 🛳 Self Hosting
   Mintplex Labs & the community maintain a number of deployment methods, scripts, and templates that you can use to run AnythingLLM locally. Refer to the table below to read how to deploy on your prefe...
Section: How to setup for development
   - `yarn setup` To fill in the required `.env` files you'll need in each of the application sections (from root of repo).   - Go fill those out before proceeding. Ensure `server/.env.development` is f...
Section: Contributing
   - create issue - create PR with branch name format of `<issue number>-<short name>` - yee haw let's merge  ...
Section: Telemetry & Privacy
   AnythingLLM by Mintplex Labs Inc contains a telemetry feature that collects anonymous usage information.  <details> <summary><kbd>More about Telemetry & Privacy for AnythingLLM</kbd></summary>  ...
Section: Why?
   We use this information to help us understand how AnythingLLM is used, to help us prioritize work on new features and bug fixes, and to help us improve AnythingLLM's performance and stability.  ...
Section: Opting out
   Set `DISABLE_TELEMETRY` in your server or docker .env settings to "true" to opt out of telemetry. You can also do this in-app by going to the sidebar > `Privacy` and disabling telemetry.  ...
Section: What do you explicitly track?
   We will only track usage details that help us make product and roadmap decisions, specifically:  - Typ of your installation (Docker or Desktop) - When a document is added or removed. No information _...
Section: 🔗 More Products
   - **[VectorAdmin][vector-admin]:** An all-in-one GUI & tool-suite for managing vector databases. - **[OpenAI Assistant Swarm][assistant-swarm]:** Turn your entire library of OpenAI assistants into on...

## File: SECURITY.md

# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |


## Reporting a Vulnerability

If a security concern is found that you would like to disclose you can create a PR for it or if you would like to clear this issue before posting you can email [Core Mintplex Labs Team](mailto:team@mintplexlabs.com).


## File: package.json

Name: anything-llm
Version: 0.2.0
Dependencies:

## File: server/index.js

React Component: FILE_LIMIT
React Component: IndexPage
React Component: VectorDb

## File: frontend/src/App.jsx

Function: App
React Component: Main
React Component: InvitePage
React Component: WorkspaceChat
React Component: AdminUsers
React Component: AdminInvites
React Component: AdminWorkspaces
React Component: AdminSystem
React Component: AdminLogs
React Component: AdminAgents
React Component: GeneralChats
React Component: GeneralAppearance
React Component: GeneralApiKeys
React Component: GeneralLLMPreference
React Component: GeneralTranscriptionPreference
React Component: GeneralAudioPreference
React Component: GeneralEmbeddingPreference
React Component: EmbeddingTextSplitterPreference
React Component: GeneralVectorDatabase
React Component: GeneralSecurity
React Component: WorkspaceSettings
React Component: EmbedConfigSetup
React Component: EmbedChats
React Component: PrivacyAndData
React Component: ExperimentalFeatures
React Component: LiveDocumentSyncManage

## File: collector/index.js



## File: server/prisma/schema.prisma

Prisma Schema Models:
Model: api_keys
  id            Int      @id @default(autoincrement())
  secret        String?  @unique
  createdBy     Int?
  createdAt     DateTime @default(now())
  lastUpdatedAt DateTime @default(now())

Model: workspace_documents
  id                   Int                   @id @default(autoincrement())
  docId                String                @unique
  filename             String
  docpath              String
  workspaceId          Int
  metadata             String?
  pinned               Boolean?              @default(false)
  watched              Boolean?              @default(false)
  createdAt            DateTime              @default(now())
  lastUpdatedAt        DateTime              @default(now())
  workspace            workspaces            @relation(fields: [workspaceId], references: [id])
  document_sync_queues document_sync_queues?

Model: invites
  id            Int      @id @default(autoincrement())
  code          String   @unique
  status        String   @default("pending")
  claimedBy     Int?
  workspaceIds  String?
  createdAt     DateTime @default(now())
  createdBy     Int
  lastUpdatedAt DateTime @default(now())

Model: system_settings
  id            Int      @id @default(autoincrement())
  label         String   @unique
  value         String?
  createdAt     DateTime @default(now())
  lastUpdatedAt DateTime @default(now())

Model: users
  id                          Int                           @id @default(autoincrement())
  username                    String?                       @unique
  password                    String
  pfpFilename                 String?
  role                        String                        @default("default")
  suspended                   Int                           @default(0)
  seen_recovery_codes         Boolean?                      @default(false)
  createdAt                   DateTime                      @default(now())
  lastUpdatedAt               DateTime                      @default(now())
  workspace_chats             workspace_chats[]
  workspace_users             workspace_users[]
  embed_configs               embed_configs[]
  embed_chats                 embed_chats[]
  threads                     workspace_threads[]
  recovery_codes              recovery_codes[]
  password_reset_tokens       password_reset_tokens[]
  workspace_agent_invocations workspace_agent_invocations[]
  slash_command_presets       slash_command_presets[]

Model: recovery_codes
  id        Int      @id @default(autoincrement())
  user_id   Int
  code_hash String
  createdAt DateTime @default(now())
  user      users    @relation(fields: [user_id], references: [id], onDelete: Cascade)
  
  @@index([user_id])

Model: password_reset_tokens
  id        Int      @id @default(autoincrement())
  user_id   Int
  token     String   @unique
  expiresAt DateTime
  createdAt DateTime @default(now())
  user      users    @relation(fields: [user_id], references: [id], onDelete: Cascade)
  
  @@index([user_id])

Model: document_vectors
  id            Int      @id @default(autoincrement())
  docId         String
  vectorId      String
  createdAt     DateTime @default(now())
  lastUpdatedAt DateTime @default(now())

Model: welcome_messages
  id         Int      @id @default(autoincrement())
  user       String
  response   String
  orderIndex Int?
  createdAt  DateTime @default(now())

Model: workspaces
  id                           Int                            @id @default(autoincrement())
  name                         String
  slug                         String                         @unique
  vectorTag                    String?
  createdAt                    DateTime                       @default(now())
  openAiTemp                   Float?
  openAiHistory                Int                            @default(20)
  lastUpdatedAt                DateTime                       @default(now())
  openAiPrompt                 String?
  similarityThreshold          Float?                         @default(0.25)
  chatProvider                 String?
  chatModel                    String?
  topN                         Int?                           @default(4)
  chatMode                     String?                        @default("chat")
  pfpFilename                  String?
  agentProvider                String?
  agentModel                   String?
  queryRefusalResponse         String?
  workspace_users              workspace_users[]
  documents                    workspace_documents[]
  workspace_suggested_messages workspace_suggested_messages[]
  embed_configs                embed_configs[]
  threads                      workspace_threads[]
  workspace_agent_invocations  workspace_agent_invocations[]

Model: workspace_threads
  id            Int        @id @default(autoincrement())
  name          String
  slug          String     @unique
  workspace_id  Int
  user_id       Int?
  createdAt     DateTime   @default(now())
  lastUpdatedAt DateTime   @default(now())
  workspace     workspaces @relation(fields: [workspace_id], references: [id], onDelete: Cascade)
  user          users?     @relation(fields: [user_id], references: [id], onDelete: Cascade)
  
  @@index([workspace_id])
  @@index([user_id])

Model: workspace_suggested_messages
  id            Int        @id @default(autoincrement())
  workspaceId   Int
  heading       String
  message       String
  createdAt     DateTime   @default(now())
  lastUpdatedAt DateTime   @default(now())
  workspace     workspaces @relation(fields: [workspaceId], references: [id], onDelete: Cascade)
  
  @@index([workspaceId])

Model: workspace_chats
  id            Int      @id @default(autoincrement())
  workspaceId   Int
  prompt        String
  response      String
  include       Boolean  @default(true)
  user_id       Int?
  thread_id     Int? // No relation to prevent whole table migration
  createdAt     DateTime @default(now())
  lastUpdatedAt DateTime @default(now())
  feedbackScore Boolean?
  users         users?   @relation(fields: [user_id], references: [id], onDelete: Cascade, onUpdate: Cascade)

Model: workspace_agent_invocations
  id            Int        @id @default(autoincrement())
  uuid          String     @unique
  prompt        String // Contains agent invocation to parse + option additional text for seed.
  closed        Boolean    @default(false)
  user_id       Int?
  thread_id     Int? // No relation to prevent whole table migration
  workspace_id  Int
  createdAt     DateTime   @default(now())
  lastUpdatedAt DateTime   @default(now())
  user          users?     @relation(fields: [user_id], references: [id], onDelete: Cascade, onUpdate: Cascade)
  workspace     workspaces @relation(fields: [workspace_id], references: [id], onDelete: Cascade, onUpdate: Cascade)
  
  @@index([uuid])

Model: workspace_users
  id            Int        @id @default(autoincrement())
  user_id       Int
  workspace_id  Int
  createdAt     DateTime   @default(now())
  lastUpdatedAt DateTime   @default(now())
  workspaces    workspaces @relation(fields: [workspace_id], references: [id], onDelete: Cascade, onUpdate: Cascade)
  users         users      @relation(fields: [user_id], references: [id], onDelete: Cascade, onUpdate: Cascade)

Model: cache_data
  id            Int       @id @default(autoincrement())
  name          String
  data          String
  belongsTo     String?
  byId          Int?
  expiresAt     DateTime?
  createdAt     DateTime  @default(now())
  lastUpdatedAt DateTime  @default(now())

Model: embed_configs
  id                         Int           @id @default(autoincrement())
  uuid                       String        @unique
  enabled                    Boolean       @default(false)
  chat_mode                  String        @default("query")
  allowlist_domains          String?
  allow_model_override       Boolean       @default(false)
  allow_temperature_override Boolean       @default(false)
  allow_prompt_override      Boolean       @default(false)
  max_chats_per_day          Int?
  max_chats_per_session      Int?
  workspace_id               Int
  createdBy                  Int?
  usersId                    Int?
  createdAt                  DateTime      @default(now())
  workspace                  workspaces    @relation(fields: [workspace_id], references: [id], onDelete: Cascade)
  embed_chats                embed_chats[]
  users                      users?        @relation(fields: [usersId], references: [id])

Model: embed_chats
  id                     Int           @id @default(autoincrement())
  prompt                 String
  response               String
  session_id             String
  include                Boolean       @default(true)
  connection_information String?
  embed_id               Int
  usersId                Int?
  createdAt              DateTime      @default(now())
  embed_config           embed_configs @relation(fields: [embed_id], references: [id], onDelete: Cascade)
  users                  users?        @relation(fields: [usersId], references: [id])

Model: event_logs
  id         Int      @id @default(autoincrement())
  event      String
  metadata   String?
  userId     Int?
  occurredAt DateTime @default(now())
  
  @@index([event])

Model: slash_command_presets
  id            Int      @id @default(autoincrement())
  command       String
  prompt        String
  description   String
  uid           Int      @default(0) // 0 is null user
  userId        Int?
  createdAt     DateTime @default(now())
  lastUpdatedAt DateTime @default(now())
  user          users?   @relation(fields: [userId], references: [id], onDelete: Cascade)
  
  @@unique([uid, command])

Model: document_sync_queues
  id             Int                        @id @default(autoincrement())
  staleAfterMs   Int                        @default(604800000) // 7 days
  nextSyncAt     DateTime
  createdAt      DateTime                   @default(now())
  lastSyncedAt   DateTime                   @default(now())
  workspaceDocId Int                        @unique
  workspaceDoc   workspace_documents?       @relation(fields: [workspaceDocId], references: [id], onDelete: Cascade)
  runs           document_sync_executions[]

Model: document_sync_executions
  id        Int                  @id @default(autoincrement())
  queueId   Int
  status    String               @default("unknown")
  result    String?
  createdAt DateTime             @default(now())
  queue     document_sync_queues @relation(fields: [queueId], references: [id], onDelete: Cascade)


## Directory: server/utils

```
├── AiProviders
│   ├── anthropic
│   │   └── index.js
│   ├── azureOpenAi
│   │   └── index.js
│   ├── cohere
│   │   └── index.js
│   ├── gemini
│   │   └── index.js
│   ├── genericOpenAi
│   │   └── index.js
│   ├── groq
│   │   └── index.js
│   ├── huggingface
│   │   └── index.js
│   ├── koboldCPP
│   │   └── index.js
│   ├── liteLLM
│   │   └── index.js
│   ├── lmStudio
│   │   └── index.js
│   ├── localAi
│   │   └── index.js
│   ├── mistral
│   │   └── index.js
│   ├── native
│   │   └── index.js
│   ├── ollama
│   │   ├── README.md
│   │   └── index.js
│   ├── openAi
│   │   └── index.js
│   ├── openRouter
│   │   └── index.js
│   ├── perplexity
│   │   ├── index.js
│   │   ├── models.js
│   │   └── scripts
│   │   │   ├── .gitignore
│   │   │   ├── chat_models.txt
│   │   │   └── parse.mjs
│   ├── textGenWebUI
│   │   └── index.js
│   └── togetherAi
│   │   ├── index.js
│   │   ├── models.js
│   │   └── scripts
│   │   │   ├── .gitignore
│   │   │   ├── chat_models.txt
│   │   │   └── parse.mjs
├── BackgroundWorkers
│   └── index.js
├── DocumentManager
│   └── index.js
├── EmbeddingEngines
│   ├── azureOpenAi
│   │   └── index.js
│   ├── cohere
│   │   └── index.js
│   ├── genericOpenAi
│   │   └── index.js
│   ├── liteLLM
│   │   └── index.js
│   ├── lmstudio
│   │   └── index.js
│   ├── localAi
│   │   └── index.js
│   ├── native
│   │   └── index.js
│   ├── ollama
│   │   └── index.js
│   ├── openAi
│   │   └── index.js
│   └── voyageAi
│   │   └── index.js
├── EncryptionManager
│   └── index.js
├── PasswordRecovery
│   └── index.js
├── TextSplitter
│   └── index.js
├── TextToSpeech
│   ├── elevenLabs
│   │   └── index.js
│   ├── index.js
│   └── openAi
│   │   └── index.js
├── agents
│   ├── aibitat
│   │   ├── error.js
│   │   ├── example
│   │   │   ├── .gitignore
│   │   │   ├── beginner-chat.js
│   │   │   ├── blog-post-coding.js
│   │   │   └── websocket
│   │   │   │   ├── index.html
│   │   │   │   ├── websock-branding-collab.js
│   │   │   │   └── websock-multi-turn-chat.js
│   │   ├── index.js
│   │   ├── plugins
│   │   │   ├── chat-history.js
│   │   │   ├── cli.js
│   │   │   ├── file-history.js
│   │   │   ├── index.js
│   │   │   ├── memory.js
│   │   │   ├── rechart.js
│   │   │   ├── save-file-browser.js
│   │   │   ├── sql-agent
│   │   │   │   ├── SQLConnectors
│   │   │   │   │   ├── MSSQL.js
│   │   │   │   │   ├── MySQL.js
│   │   │   │   │   ├── Postgresql.js
│   │   │   │   │   └── index.js
│   │   │   │   ├── get-table-schema.js
│   │   │   │   ├── index.js
│   │   │   │   ├── list-database.js
│   │   │   │   ├── list-table.js
│   │   │   │   └── query.js
│   │   │   ├── summarize.js
│   │   │   ├── web-browsing.js
│   │   │   ├── web-scraping.js
│   │   │   └── websocket.js
│   │   ├── providers
│   │   │   ├── ai-provider.js
│   │   │   ├── anthropic.js
│   │   │   ├── azure.js
│   │   │   ├── genericOpenAi.js
│   │   │   ├── groq.js
│   │   │   ├── helpers
│   │   │   │   ├── classes.js
│   │   │   │   └── untooled.js
│   │   │   ├── index.js
│   │   │   ├── koboldcpp.js
│   │   │   ├── lmstudio.js
│   │   │   ├── localai.js
│   │   │   ├── mistral.js
│   │   │   ├── ollama.js
│   │   │   ├── openai.js
│   │   │   ├── openrouter.js
│   │   │   ├── perplexity.js
│   │   │   ├── textgenwebui.js
│   │   │   └── togetherai.js
│   │   └── utils
│   │   │   ├── dedupe.js
│   │   │   └── summarize.js
│   ├── defaults.js
│   └── index.js
├── boot
│   ├── MetaGenerator.js
│   └── index.js
├── chats
│   ├── agents.js
│   ├── commands
│   │   └── reset.js
│   ├── embed.js
│   ├── index.js
│   ├── openaiCompatible.js
│   └── stream.js
├── collectorApi
│   └── index.js
├── comKey
│   └── index.js
├── database
│   └── index.js
├── files
│   ├── index.js
│   ├── logo.js
│   ├── multer.js
│   ├── pfp.js
│   └── purgeDocument.js
├── helpers
│   ├── admin
│   │   └── index.js
│   ├── camelcase.js
│   ├── chat
│   │   ├── convertTo.js
│   │   ├── index.js
│   │   └── responses.js
│   ├── customModels.js
│   ├── index.js
│   ├── portAvailabilityChecker.js
│   ├── tiktoken.js
│   └── updateENV.js
├── http
│   └── index.js
├── logger
│   └── index.js
├── middleware
│   ├── embedMiddleware.js
│   ├── featureFlagEnabled.js
│   ├── multiUserProtected.js
│   ├── validApiKey.js
│   ├── validWorkspace.js
│   └── validatedRequest.js
├── prisma
│   ├── PRISMA.md
│   ├── index.js
│   └── migrateFromSqlite.js
├── telemetry
│   └── index.js
└── vectorDbProviders
│   ├── astra
│   │   ├── ASTRA_SETUP.md
│   │   └── index.js
│   ├── chroma
│   │   ├── CHROMA_SETUP.md
│   │   └── index.js
│   ├── lance
│   │   └── index.js
│   ├── milvus
│   │   ├── MILVUS_SETUP.md
│   │   └── index.js
│   ├── pinecone
│   │   ├── PINECONE_SETUP.md
│   │   └── index.js
│   ├── qdrant
│   │   ├── QDRANT_SETUP.md
│   │   └── index.js
│   ├── weaviate
│   │   ├── WEAVIATE_SETUP.md
│   │   └── index.js
│   └── zilliz
│   │   └── index.js
```



## File: server/utils/EmbeddingEngines/lmstudio/index.js

Class: LMStudioEmbedder

## File: server/utils/EmbeddingEngines/voyageAi/index.js

Class: VoyageAiEmbedder

## File: server/utils/EmbeddingEngines/cohere/index.js

Class: CohereEmbedder

## File: server/utils/EmbeddingEngines/native/index.js

Function: will
Function: will
Function: pipeline
Class: NativeEmbedder

## File: server/utils/EmbeddingEngines/azureOpenAi/index.js

Class: AzureOpenAiEmbedder

## File: server/utils/EmbeddingEngines/localAi/index.js

Class: LocalAiEmbedder

## File: server/utils/EmbeddingEngines/genericOpenAi/index.js

Class: GenericOpenAiEmbedder
Class: with

## File: server/utils/EmbeddingEngines/ollama/index.js

Class: OllamaEmbedder

## File: server/utils/EmbeddingEngines/liteLLM/index.js

Class: LiteLLMEmbedder

## File: server/utils/EmbeddingEngines/openAi/index.js

Class: OpenAiEmbedder

## File: server/utils/middleware/validWorkspace.js

Function: validWorkspaceSlug
Function: validWorkspaceAndThreadSlug

## File: server/utils/middleware/featureFlagEnabled.js

Function: featureFlagEnabled

## File: server/utils/middleware/multiUserProtected.js

Function: strictMultiUserRoleValid
Function: flexUserRoleValid
Function: isMultiUserSetup
React Component: ROLES
React Component: DEFAULT_ROLES

## File: server/utils/middleware/validatedRequest.js

Function: validatedRequest
Function: validateMultiUserRequest

## File: server/utils/middleware/validApiKey.js

Function: validApiKey

## File: server/utils/middleware/embedMiddleware.js

Function: validEmbedConfig
Function: setConnectionMeta
Function: validEmbedConfigId
Function: canRespond

## File: server/utils/database/index.js

Function: checkColumnTemplate
Function: checkForMigrations
Function: tries
Function: will
Function: validateTablePragmas
Function: setupTelemetry

## File: server/utils/PasswordRecovery/index.js

Function: generateRecoveryCodes
Function: recoverAccount
Function: resetPassword

## File: server/utils/logger/index.js

Function: formatArgs
Function: setLogger
Class: Logger

## File: server/utils/boot/MetaGenerator.js

Function: is
Class: serves
Class: should
Class: does
Class: is
Class: and
Class: MetaGenerator

## File: server/utils/boot/index.js

Function: bootSSL
Function: bootHTTP
Function: catchSigTerms

## File: server/utils/EncryptionManager/index.js

Class: EncryptionManager

## File: server/utils/DocumentManager/index.js

Class: DocumentManager

## File: server/utils/prisma/PRISMA.md

# Prisma Setup and Usage Guide

This guide will help you set up and use Prisma for the project. Prisma is a powerful ORM for Node.js and TypeScript, helping developers build faster and make fewer errors. Follow the guide to understand how to use Prisma and the scripts available in the project to manage the Prisma setup.

## Setting Up Prisma

To get started with setting up Prisma, you should run the setup script from the project root directory:

```sh
yarn setup
```

This script will install the necessary node modules in both the server and frontend directories, set up the environment files, and set up Prisma (generate client, run migrations, and seed the database).

## Prisma Scripts

In the project root's `package.json`, there are several scripts set up to help you manage Prisma:

- **prisma:generate**: Generates the Prisma client.
- **prisma:migrate**: Runs the migrations to ensure the database is in sync with the schema.
- **prisma:seed**: Seeds the database with initial data.
- **prisma:setup**: A convenience script that runs `prisma:generate`, `prisma:migrate`, and `prisma:seed` in sequence.
- **sqlite:migrate**: (To be run from the `server` directory) This script is for users transitioning from the old SQLite custom ORM setup to Prisma and will migrate all exisiting data over to Prisma. If you're a new user, your setup will already use Prisma.

To run any of these scripts, use `yarn` followed by the script name from the project root directory. For example:

```sh
yarn prisma:setup
```

## Manual Prisma Commands

While the scripts should cover most of your needs, you may sometimes want to run Prisma commands manually. Here are some commands you might find useful, along with their descriptions:

- `npx prisma introspect`: Introspects the database to update the Prisma schema by reading the schema of the existing database.
- `npx prisma generate`: Generates the Prisma client.
- `npx prisma migrate dev --name init`: Ensures the database is in sync with the schema, naming the migration 'init'.
- `npx prisma migrate reset`: Resets the database, deleting all data and recreating the schema.

These commands should be run from the `server` directory, where the Prisma schema is located.

## Notes

- Always make sure to run scripts from the root level to avoid path issues.
- Before running migrations, ensure that the Prisma schema is correctly defined to prevent data loss or corruption.
- If you are adding a new feature or making changes that require a change in the database schema, create a new migration rather than editing existing migrations.
- For users transitioning from the old SQLite ORM, navigate to the `server` directory and run the `sqlite:migrate` script to smoothly transition to Prisma. If you're setting up the project fresh, this step is unnecessary as the setup will already be using Prisma.


## File: server/utils/prisma/index.js



## File: server/utils/prisma/migrateFromSqlite.js

Function: backupDatabase
Function: resetAndMigrateDatabase
Function: migrateData
Function: migrateTable
React Component: DATABASE_PATH
React Component: BACKUP_PATH

## File: server/utils/agents/index.js

Function: or
Class: AgentHandler
React Component: AIbitat
React Component: AgentPlugins
React Component: AIbitatPlugin

## File: server/utils/agents/defaults.js

React Component: AgentPlugins
React Component: Provider
React Component: USER_AGENT
React Component: WORKSPACE_AGENT

## File: server/utils/agents/aibitat/index.js

Function: for
Function: name
Function: and
Function: to
Function: configuration
Class: that
Class: AIbitat
React Component: Providers

## File: server/utils/agents/aibitat/error.js

Class: AIbitatError
Class: APIError
Class: RetryError

## File: server/utils/agents/aibitat/plugins/web-scraping.js

Function: call
React Component: Provider

## File: server/utils/agents/aibitat/plugins/web-browsing.js

Function: call

## File: server/utils/agents/aibitat/plugins/summarize.js

Function: call
React Component: Provider

## File: server/utils/agents/aibitat/plugins/memory.js

React Component: LLMConnector

## File: server/utils/agents/aibitat/plugins/index.js



## File: server/utils/agents/aibitat/plugins/file-history.js



## File: server/utils/agents/aibitat/plugins/websocket.js

Function: for
React Component: SOCKET_TIMEOUT_MS
React Component: WEBSOCKET_BAIL_COMMANDS

## File: server/utils/agents/aibitat/plugins/chat-history.js



## File: server/utils/agents/aibitat/plugins/cli.js



## File: server/utils/agents/aibitat/plugins/save-file-browser.js



## File: server/utils/agents/aibitat/plugins/rechart.js

Function: completed
Function: again
Function: completed

## File: server/utils/agents/aibitat/plugins/sql-agent/query.js



## File: server/utils/agents/aibitat/plugins/sql-agent/index.js



## File: server/utils/agents/aibitat/plugins/sql-agent/list-database.js



## File: server/utils/agents/aibitat/plugins/sql-agent/list-table.js



## File: server/utils/agents/aibitat/plugins/sql-agent/get-table-schema.js



## File: server/utils/agents/aibitat/plugins/sql-agent/SQLConnectors/Postgresql.js

Class: PostgresSQLConnector

## File: server/utils/agents/aibitat/plugins/sql-agent/SQLConnectors/index.js

Function: getDBClient
Function: listSQLConnections

## File: server/utils/agents/aibitat/plugins/sql-agent/SQLConnectors/MSSQL.js

Class: MSSQLConnector
React Component: UrlPattern

## File: server/utils/agents/aibitat/plugins/sql-agent/SQLConnectors/MySQL.js

Class: MySQLConnector
React Component: UrlPattern

## File: server/utils/agents/aibitat/example/blog-post-coding.js

Function: main
React Component: AIbitat

## File: server/utils/agents/aibitat/example/beginner-chat.js

Function: main
React Component: AIbitat
React Component: Agent

## File: server/utils/agents/aibitat/example/websocket/websock-branding-collab.js

Function: if
Function: runAIbitat
React Component: AIbitat

## File: server/utils/agents/aibitat/example/websocket/websock-multi-turn-chat.js

Function: if
Function: runAIbitat
React Component: AIbitat
React Component: Agent

## File: server/utils/agents/aibitat/providers/genericOpenAi.js

Function: over
Class: GenericOpenAiProvider
Class: inherited
React Component: OpenAI
React Component: Provider
React Component: InheritMultiple
React Component: UnTooled

## File: server/utils/agents/aibitat/providers/localai.js

Function: over
Class: LocalAiProvider
Class: inherited
React Component: OpenAI
React Component: Provider
React Component: InheritMultiple
React Component: UnTooled

## File: server/utils/agents/aibitat/providers/azure.js

Function: over
Class: AzureOpenAiProvider
Class: inherited
React Component: Provider
React Component: InheritMultiple
React Component: UnTooled

## File: server/utils/agents/aibitat/providers/openrouter.js

Function: over
Class: OpenRouterProvider
Class: inherited
React Component: OpenAI
React Component: Provider
React Component: InheritMultiple
React Component: UnTooled

## File: server/utils/agents/aibitat/providers/perplexity.js

Function: over
Class: PerplexityProvider
Class: inherited
React Component: OpenAI
React Component: Provider
React Component: InheritMultiple
React Component: UnTooled

## File: server/utils/agents/aibitat/providers/textgenwebui.js

Function: over
Class: TextWebGenUiProvider
Class: inherited
React Component: OpenAI
React Component: Provider
React Component: InheritMultiple
React Component: UnTooled

## File: server/utils/agents/aibitat/providers/lmstudio.js

Function: over
Class: LMStudioProvider
Class: inherited
React Component: OpenAI
React Component: Provider
React Component: InheritMultiple
React Component: UnTooled

## File: server/utils/agents/aibitat/providers/index.js

React Component: OpenAIProvider
React Component: AnthropicProvider
React Component: LMStudioProvider
React Component: OllamaProvider
React Component: GroqProvider
React Component: TogetherAIProvider
React Component: AzureOpenAiProvider
React Component: KoboldCPPProvider
React Component: LocalAIProvider
React Component: OpenRouterProvider
React Component: MistralProvider
React Component: GenericOpenAiProvider
React Component: PerplexityProvider
React Component: TextWebGenUiProvider

## File: server/utils/agents/aibitat/providers/mistral.js

Function: over
Class: MistralProvider
Class: inherited
React Component: OpenAI
React Component: Provider
React Component: InheritMultiple
React Component: UnTooled

## File: server/utils/agents/aibitat/providers/ai-provider.js

Class: Provider
React Component: DEFAULT_WORKSPACE_PROMPT

## File: server/utils/agents/aibitat/providers/ollama.js

Function: over
Class: OllamaProvider
Class: inherited
React Component: Provider
React Component: InheritMultiple
React Component: UnTooled

## File: server/utils/agents/aibitat/providers/openai.js

Function: calls
Function: again
Class: OpenAIProvider
React Component: OpenAI
React Component: Provider

## File: server/utils/agents/aibitat/providers/togetherai.js

Function: over
Class: TogetherAIProvider
Class: inherited
React Component: OpenAI
React Component: Provider
React Component: InheritMultiple
React Component: UnTooled

## File: server/utils/agents/aibitat/providers/groq.js

Function: over
Class: GroqProvider
Class: inherited
React Component: OpenAI
React Component: Provider
React Component: InheritMultiple
React Component: UnTooled

## File: server/utils/agents/aibitat/providers/koboldcpp.js

Function: over
Class: KoboldCPPProvider
Class: inherited
React Component: OpenAI
React Component: Provider
React Component: InheritMultiple
React Component: UnTooled

## File: server/utils/agents/aibitat/providers/anthropic.js

Function: can
Class: AnthropicProvider
React Component: Anthropic
React Component: Provider

## File: server/utils/agents/aibitat/providers/helpers/classes.js

Function: InheritMultiple
Class: Bases

## File: server/utils/agents/aibitat/providers/helpers/untooled.js

Function: vKey
Function: call
Function: and
Function: is
Function: to
Function: that
Function: name
Function: properties
Function: if
Function: tool
Class: for
Class: UnTooled

## File: server/utils/agents/aibitat/utils/dedupe.js

Function: many
Function: name
Class: Deduplicator
React Component: DEFAULT_COOLDOWN_MS

## File: server/utils/agents/aibitat/utils/summarize.js

Function: summarizeContent
Function: creates
React Component: Provider

## File: server/utils/vectorDbProviders/chroma/index.js

React Component: COLLECTION_REGEX
React Component: Chroma
React Component: EmbedderEngine

## File: server/utils/vectorDbProviders/chroma/CHROMA_SETUP.md

# How to setup a local (or remote) Chroma Vector Database

[Official Chroma Docs](https://docs.trychroma.com/guides#running-chroma-in-clientserver-mode) for reference.

### How to get started

**Requirements**

- Docker
- `git` available in your CLI/terminal

**Instructions**

- `git clone git@github.com:chroma-core/chroma.git` to somewhere on computer.
- `cd chroma`
- `docker-compose up -d --build`
- set the `CHROMA_ENDPOINT=` .env variable in `server` and also set `VECTOR_DB=` to `chroma`.

* If you have an API Gateway or auth middleway be sure to set the `CHROMA_API_HEADER` and `CHROMA_API_KEY` keys.

eg: `server/.env.development`

```
VECTOR_DB="chroma"
CHROMA_ENDPOINT='http://localhost:8000'
# CHROMA_API_HEADER="X-Api-Key" // If you have an Auth middleware on your instance.
# CHROMA_API_KEY="sk-123abc" // If you have an Auth middleware on your instance.
```


## File: server/utils/vectorDbProviders/lance/index.js

React Component: LanceDb
React Component: EmbedderEngine

## File: server/utils/vectorDbProviders/pinecone/PINECONE_SETUP.md

# How to setup Pinecone Vector Database for AnythingLLM

[Official Pinecone Docs](https://docs.pinecone.io/docs/overview) for reference.

### How to get started

**Requirements**

- Pinecone account with index that allows namespaces.

**Note:** [Namespaces are not supported in `gcp-starter` environments](https://docs.pinecone.io/docs/namespaces) and are required to work with AnythingLLM.

**Instructions**

- Create an index on your Pinecone account. Name can be anything eg: `my-primary-index`
- Metric `cosine`
- Dimensions `1536` since we use OpenAI for embeddings
- 1 pod, all other default settings are fine.

```
VECTOR_DB="pinecone"
PINECONE_API_KEY=sklive-123xyz
PINECONE_INDEX=my-primary-index # the value from the first instruction!
```


## File: server/utils/vectorDbProviders/pinecone/index.js

React Component: PineconeDB
React Component: EmbedderEngine

## File: server/utils/vectorDbProviders/qdrant/QDRANT_SETUP.md

# How to setup a local (or cloud) QDrant Vector Database

[Get a QDrant Cloud instance](https://cloud.qdrant.io/).
[Set up QDrant locally on Docker](https://github.com/qdrant/qdrant/blob/master/QUICK_START.md).

Fill out the variables in the "Vector Database" tab of settings. Select Qdrant as your provider and fill out the appropriate fields
with the information from either of the above steps.

### How to get started _Development mode only_

After setting up either the Qdrant cloud or local dockerized instance you just need to set these variable in `.env.development` or defined them at runtime via the UI.

```
# VECTOR_DB="qdrant"
# QDRANT_ENDPOINT="https://<YOUR_CLOUD_INSTANCE_URL>.qdrant.io:6333"
# QDRANT_API_KEY="abc...123xyz"
```


## File: server/utils/vectorDbProviders/qdrant/index.js

React Component: QDrant
React Component: EmbedderEngine

## File: server/utils/vectorDbProviders/zilliz/index.js

Class: with
React Component: Zilliz
React Component: EmbedderEngine

## File: server/utils/vectorDbProviders/astra/index.js

React Component: AstraDB
React Component: EmbedderEngine

## File: server/utils/vectorDbProviders/astra/ASTRA_SETUP.md

# How to setup Astra Vector Database for AnythingLLM

[Official Astra DB Docs](https://docs.datastax.com/en/astra/astra-db-vector/get-started/quickstart.html) for reference.

### How to get started

**Requirements**

- Astra Vector Database with active status.

**Instructions**

- [Create an Astra account or sign in to an existing Astra account](https://astra.datastax.com)
- Create an Astra Serverless(Vector) Database.
- Make sure DB is in active state.
- Get `API ENDPOINT`and `Application Token` from Overview screen

```
VECTOR_DB="astra"
ASTRA_DB_ENDPOINT=Astra DB API endpoint
ASTRA_DB_APPLICATION_TOKEN=AstraCS:..
```


## File: server/utils/vectorDbProviders/weaviate/index.js

Function: is
React Component: Weaviate
React Component: EmbedderEngine

## File: server/utils/vectorDbProviders/weaviate/WEAVIATE_SETUP.md

# How to setup a local (or cloud) Weaviate Vector Database

[Get a Weaviate Cloud instance](https://weaviate.io/developers/weaviate/quickstart#create-an-instance).
[Set up Weaviate locally on Docker](https://weaviate.io/developers/weaviate/installation/docker-compose).

Fill out the variables in the "Vector Database" tab of settings. Select Weaviate as your provider and fill out the appropriate fields
with the information from either of the above steps.

### How to get started _Development mode only_

After setting up either the Weaviate cloud or local dockerized instance you just need to set these variable in `.env.development` or defined them at runtime via the UI.

```
VECTOR_DB="weaviate"
WEAVIATE_ENDPOINT='http://localhost:8080'
WEAVIATE_API_KEY= # Optional
```


## File: server/utils/vectorDbProviders/milvus/index.js

React Component: Milvus
React Component: EmbedderEngine

## File: server/utils/vectorDbProviders/milvus/MILVUS_SETUP.md

# How to setup a local (or remote) Milvus Vector Database

[Official Milvus Docs](https://milvus.io/docs/example_code.md) for reference.

### How to get started

**Requirements**

Choose one of the following

- Cloud

  - [Cloud account](https://cloud.zilliz.com/)

- Local
  - Docker
  - `git` available in your CLI/terminal

**Instructions**

- Cloud

  - Create a Cluster on your cloud account
  - Get connect Public Endpoint and Token
  - Set .env.development variable in server

- Local
  - Download yaml file `wget https://github.com/milvus-io/milvus/releases/download/v2.3.4/milvus-standalone-docker-compose.yml -O docker-compose.yml`
  - Start Milvus `sudo docker compose up -d`
  - Check the containers are up and running `sudo docker compose ps`
  - Get port number and set .env.development variable in server

eg: `server/.env.development`

```
VECTOR_DB="milvus"
MILVUS_ADDRESS="http://localhost:19530"
MILVUS_USERNAME=minioadmin # Whatever your username and password are
MILVUS_PASSWORD=minioadmin
```


## File: server/utils/comKey/index.js

Class: do
Class: generates
Class: and
Class: CommunicationKey
Class: and
Class: of
Class: only

## File: server/utils/AiProviders/lmStudio/index.js

Class: LMStudioLLM

## File: server/utils/AiProviders/textGenWebUI/index.js

Class: TextGenWebUILLM

## File: server/utils/AiProviders/cohere/index.js

Function: handleAbort
Class: CohereLLM

## File: server/utils/AiProviders/togetherAi/index.js

Function: togetherAiModels
Class: TogetherAiLLM

## File: server/utils/AiProviders/togetherAi/models.js

React Component: MODELS

## File: server/utils/AiProviders/gemini/index.js

Function: handleAbort
Class: GeminiLLM

## File: server/utils/AiProviders/openRouter/index.js

Function: fetchOpenRouterModels
Function: handleAbort
Class: OpenRouterLLM
React Component: MAX_STALE

## File: server/utils/AiProviders/native/index.js

Function: ChatLlamaCpp
Function: handleAbort
Class: NativeLLM
React Component: ChatLlamaCpp
React Component: MessageClass

## File: server/utils/AiProviders/azureOpenAi/index.js

Function: handleAbort
Class: AzureOpenAiLLM

## File: server/utils/AiProviders/localAi/index.js

Class: LocalAiLLM

## File: server/utils/AiProviders/koboldCPP/index.js

Function: handleAbort
Class: KoboldCPPLLM

## File: server/utils/AiProviders/groq/index.js

Class: GroqLLM

## File: server/utils/AiProviders/genericOpenAi/index.js

Class: GenericOpenAiLLM

## File: server/utils/AiProviders/perplexity/index.js

Function: perplexityModels
Class: PerplexityLLM

## File: server/utils/AiProviders/perplexity/models.js

React Component: MODELS

## File: server/utils/AiProviders/anthropic/index.js

Function: handleAbort
Function: parseErrorMsg
Class: AnthropicLLM
React Component: AnthropicAI

## File: server/utils/AiProviders/huggingface/index.js

Class: HuggingFaceLLM

## File: server/utils/AiProviders/ollama/index.js

Function: handleAbort
Class: OllamaAILLM
React Component: MessageClass

## File: server/utils/AiProviders/ollama/README.md

# Common Issues with Ollama

If you encounter an error stating `llama:streaming - could not stream chat. Error: connect ECONNREFUSED 172.17.0.1:11434` when using AnythingLLM in a Docker container, this indicates that the IP of the Host inside of the virtual docker network does not bind to port 11434 of the host system by default, due to Ollama's restriction to localhost and 127.0.0.1. To resolve this issue and ensure proper communication between the Dockerized AnythingLLM and the Ollama service, you must configure Ollama to bind to 0.0.0.0 or a specific IP address.

### Setting Environment Variables on Mac

If Ollama is run as a macOS application, environment variables should be set using `launchctl`:

1.  For each environment variable, call `launchctl setenv`.
    ```bash
    launchctl setenv OLLAMA_HOST "0.0.0.0"
    ```
2.  Restart the Ollama application.

### Setting Environment Variables on Linux

If Ollama is run as a systemd service, environment variables should be set using `systemctl`:

1.  Edit the systemd service by calling `systemctl edit ollama.service`. This will open an editor.
2.  For each environment variable, add a line `Environment` under the section `[Service]`:
    ```ini
    [Service]
    Environment="OLLAMA_HOST=0.0.0.0"
    ```
3.  Save and exit.
4.  Reload `systemd` and restart Ollama:
    ```bash
    systemctl daemon-reload
    systemctl restart ollama
    ```

### Setting Environment Variables on Windows

On Windows, Ollama inherits your user and system environment variables.

1.  First, quit Ollama by clicking on it in the taskbar.
2.  Edit system environment variables from the Control Panel.
3.  Edit or create new variable(s) for your user account for `OLLAMA_HOST`, `OLLAMA_MODELS`, etc.
4.  Click OK/Apply to save.
5.  Run `ollama` from a new terminal window.


## File: server/utils/AiProviders/liteLLM/index.js

Class: LiteLLM

## File: server/utils/AiProviders/mistral/index.js

Class: MistralLLM

## File: server/utils/AiProviders/openAi/index.js

Class: OpenAiLLM

## File: server/utils/http/index.js

Function: reqBody
Function: queryParams
Function: makeJWT
Function: userFromSession
Function: decodeJWT
Function: multiUserMode
Function: parseAuthHeader
Function: safeJsonParse
Function: isValidUrl
Function: toValidNumber
React Component: JWT

## File: server/utils/TextSplitter/index.js

Function: isNullOrNaN
Class: TextSplitter
Class: RecursiveSplitter

## File: server/utils/collectorApi/index.js

Function: to
Class: CollectorApi

## File: server/utils/files/index.js

Function: fileData
Function: viewLocalFiles
Function: cachedVectorInformation
Function: storeVectorResult
Function: purgeSourceDocument
Function: purgeVectorCache
Function: findDocumentInDocuments
Function: isWithin
Function: normalizePath
Function: hasVectorCachedFiles

## File: server/utils/files/pfp.js

Function: fetchPfp
Function: determinePfpFilepath
Function: determineWorkspacePfpFilepath

## File: server/utils/files/logo.js

Function: validFilename
Function: getDefaultFilename
Function: determineLogoFilepath
Function: fetchLogo
Function: renameLogoFile
Function: removeCustomLogo
React Component: LOGO_FILENAME

## File: server/utils/files/purgeDocument.js

Function: purgeDocument
Function: purgeFolder
Function: rmVectorCache
Function: rmWorkspaceDoc

## File: server/utils/files/multer.js

Function: handleFileUpload
Function: handleAssetUpload
Function: handlePfpUpload

## File: server/utils/TextToSpeech/index.js

Function: getTTSProvider

## File: server/utils/TextToSpeech/elevenLabs/index.js

Class: ElevenLabsTTS

## File: server/utils/TextToSpeech/openAi/index.js

Class: OpenAiTTS

## File: server/utils/chats/openaiCompatible.js

Function: chatSync
Function: streamChat
Function: formatJSON
React Component: LLMConnector
React Component: VectorDb
React Component: LLMConnector
React Component: VectorDb

## File: server/utils/chats/agents.js

Function: grepAgents

## File: server/utils/chats/stream.js

Function: streamChatWithWorkspace
React Component: VALID_CHAT_MODE
React Component: LLMConnector
React Component: VectorDb

## File: server/utils/chats/index.js

Function: grepCommand
Function: chatWithWorkspace
Function: recentChatHistory
Function: chatPrompt
Function: to
Function: sourceIdentifier
React Component: VALID_COMMANDS
React Component: LLMConnector
React Component: VectorDb

## File: server/utils/chats/embed.js

Function: streamChatWithForEmbed
Function: recentEmbedChatHistory
React Component: LLMConnector
React Component: VectorDb

## File: server/utils/chats/commands/reset.js

Function: resetMemory

## File: server/utils/telemetry/index.js

Function: setupTelemetry

## File: server/utils/BackgroundWorkers/index.js

Class: BackgroundService
React Component: Graceful
React Component: Bree

## File: server/utils/helpers/tiktoken.js

Class: TokenManager

## File: server/utils/helpers/portAvailabilityChecker.js

Function: getLocalHosts
Function: checkPort
Function: isPortInUse

## File: server/utils/helpers/updateENV.js

Function: isNotEmpty
Function: nonZero
Function: isValidURL
Function: validOpenAIKey
Function: validAnthropicApiKey
Function: validLLMExternalBasePath
Function: validOllamaLLMBasePath
Function: supportedTTSProvider
Function: validLocalWhisper
Function: supportedLLM
Function: supportedTranscriptionProvider
Function: validGeminiModel
Function: validGeminiSafetySetting
Function: validAnthropicModel
Function: supportedEmbeddingModel
Function: supportedVectorDB
Function: validChromaURL
Function: validOpenAiTokenLimit
Function: requiresForceMode
Function: isDownloadedModel
Function: validDockerizedUrl
Function: validHuggingFaceEndpoint
Function: noRestrictedChars
Function: updateENV
Function: executeValidationChecks
Function: logChangesToEventLog
Function: dumpENV
Function: sanitizeValue
React Component: KEY_MAPPING
React Component: ENV_KEYS

## File: server/utils/helpers/index.js

Function: getVectorDbClass
Function: getLLMProvider
Function: getEmbeddingEngineSelection
Function: maximumChunkLength
Function: toChunks
React Component: LLMSelection

## File: server/utils/helpers/camelcase.js

Function: camelCase
Function: preserveCamelCase
Function: preserveConsecutiveUppercase
Function: postProcess
React Component: UPPERCASE
React Component: LOWERCASE
React Component: LEADING_CAPITAL
React Component: IDENTIFIER
React Component: SEPARATORS
React Component: LEADING_SEPARATORS
React Component: SEPARATORS_AND_IDENTIFIER
React Component: NUMBERS_AND_IDENTIFIER

## File: server/utils/helpers/customModels.js

Function: getCustomModels
Function: openAiModels
Function: localAIModels
Function: liteLLMModels
Function: getLMStudioModels
Function: getKoboldCPPModels
Function: ollamaAIModels
Function: getTogetherAiModels
Function: getPerplexityModels
Function: getOpenRouterModels
Function: getMistralModels
Function: nativeLLMModels
Function: getElevenLabsModels
React Component: SUPPORT_CUSTOM_MODELS

## File: server/utils/helpers/chat/convertTo.js

Function: convertToCSV
Function: convertToJSON
Function: convertToJSONAlpaca
Function: convertToJSONL
Function: prepareWorkspaceChatsForExport
Function: escapeCsv
Function: exportChatsAsType
Function: buildSystemPrompt
React Component: STANDARD_PROMPT

## File: server/utils/helpers/chat/responses.js

Function: clientAbortedHandler
Function: handleDefaultStreamResponseV2
Function: convertToChatHistory
Function: convertToPromptHistory
Function: writeResponseChunk
Function: handleAbort

## File: server/utils/helpers/chat/index.js

Function: that
Function: messageArrayCompressor
Function: messageStringCompressor
Function: cannonball
Function: is
Function: as
Function: fillSourceWindow
Function: by
Function: log

## File: server/utils/helpers/admin/index.js

Function: should
Function: validRoleSelection
Function: canModifyAdmin
Function: validCanModify

## Directory: server/models

```
├── apiKeys.js
├── cacheData.js
├── documentSyncQueue.js
├── documentSyncRun.js
├── documents.js
├── embedChats.js
├── embedConfig.js
├── eventLogs.js
├── invite.js
├── passwordRecovery.js
├── slashCommandsPresets.js
├── systemSettings.js
├── telemetry.js
├── user.js
├── vectors.js
├── welcomeMessages.js
├── workspace.js
├── workspaceAgentInvocation.js
├── workspaceChats.js
├── workspaceThread.js
├── workspaceUsers.js
└── workspacesSuggestedMessages.js
```



## File: server/models/invite.js

React Component: Invite

## File: server/models/documents.js

React Component: Document
React Component: VectorDb
React Component: VectorDb

## File: server/models/passwordRecovery.js

React Component: RecoveryCode
React Component: PasswordResetToken

## File: server/models/eventLogs.js

React Component: EventLogs

## File: server/models/cacheData.js

React Component: CacheData

## File: server/models/welcomeMessages.js

React Component: WelcomeMessages

## File: server/models/workspaceChats.js

Function: is
Function: is
Function: is
React Component: WorkspaceChats

## File: server/models/apiKeys.js

React Component: ApiKey

## File: server/models/telemetry.js

React Component: Telemetry

## File: server/models/user.js

React Component: User
React Component: VALID_ROLES

## File: server/models/vectors.js

React Component: DocumentVectors

## File: server/models/workspacesSuggestedMessages.js

React Component: WorkspaceSuggestedMessages

## File: server/models/documentSyncQueue.js

React Component: DocumentSyncQueue

## File: server/models/embedChats.js

React Component: EmbedChats

## File: server/models/workspace.js

React Component: Workspace

## File: server/models/workspaceAgentInvocation.js

React Component: WorkspaceAgentInvocation

## File: server/models/embedConfig.js

Function: validatedCreationData
React Component: EmbedConfig
React Component: BOOLEAN_KEYS
React Component: NUMBER_KEYS

## File: server/models/workspaceUsers.js

React Component: WorkspaceUser

## File: server/models/slashCommandsPresets.js

React Component: CMD_REGEX
React Component: SlashCommandPresets

## File: server/models/systemSettings.js

Function: isNullOrNaN
Function: on
Function: on
Function: on
Function: on
Function: mergeConnections
React Component: SystemSettings

## File: server/models/workspaceThread.js

React Component: WorkspaceThread

## File: server/models/documentSyncRun.js

React Component: DocumentSyncRun

## Directory: server/endpoints

```
├── admin.js
├── agentWebsocket.js
├── api
│   ├── admin
│   │   └── index.js
│   ├── auth
│   │   └── index.js
│   ├── document
│   │   └── index.js
│   ├── index.js
│   ├── openai
│   │   ├── compatibility-test-script.cjs
│   │   └── index.js
│   ├── system
│   │   └── index.js
│   ├── userManagement
│   │   └── index.js
│   ├── workspace
│   │   └── index.js
│   └── workspaceThread
│   │   └── index.js
├── chat.js
├── document.js
├── embed
│   └── index.js
├── embedManagement.js
├── experimental
│   ├── index.js
│   └── liveSync.js
├── extensions
│   └── index.js
├── invite.js
├── system.js
├── utils.js
├── workspaceThreads.js
└── workspaces.js
```



## File: server/endpoints/invite.js

Function: inviteEndpoints

API Endpoints:
  GET /invite/:code
  POST /invite/:code

## File: server/endpoints/system.js

Function: systemEndpoints
React Component: VectorDb

API Endpoints:
  GET /ping
  GET /migrate
  GET /env-dump
  GET /setup-complete
  POST /request-token
  GET /system/multi-user-mode
  GET /system/logo
  GET /system/footer-data
  GET /system/support-email
  GET /system/custom-app-name
  GET /system/is-default-logo
  GET /system/api-keys
  DELETE /system/api-key
  POST /system/user

## File: server/endpoints/workspaceThreads.js

Function: workspaceThreadEndpoints

## File: server/endpoints/embedManagement.js

Function: embedManagementEndpoints

## File: server/endpoints/workspaces.js

Function: workspaceEndpoints
React Component: Collector
React Component: Collector
React Component: VectorDb
React Component: VectorDb
React Component: TTSProvider

## File: server/endpoints/agentWebsocket.js

Function: relayToSocket
Function: agentWebsocket

## File: server/endpoints/admin.js

Function: adminEndpoints
React Component: VectorDb

## File: server/endpoints/utils.js

Function: utilEndpoints
Function: getGitVersion
Function: byteToGigaByte
Function: getDiskStorage

API Endpoints:
  GET /utils/metrics

## File: server/endpoints/chat.js

Function: chatEndpoints

## File: server/endpoints/document.js

Function: documentEndpoints

## File: server/endpoints/experimental/index.js

Function: experimentalEndpoints

## File: server/endpoints/experimental/liveSync.js

Function: liveSyncEndpoints

## File: server/endpoints/embed/index.js

Function: embeddedEndpoints

## File: server/endpoints/extensions/index.js

Function: extensionEndpoints

## File: server/endpoints/api/index.js

Function: developerEndpoints

## File: server/endpoints/api/userManagement/index.js

Function: apiUserManagementEndpoints

API Endpoints:
  GET /v1/users

## File: server/endpoints/api/auth/index.js

Function: apiAuthEndpoints

API Endpoints:
  GET /v1/auth

## File: server/endpoints/api/workspace/index.js

Function: apiWorkspaceEndpoints
React Component: VectorDb

API Endpoints:
  POST /v1/workspace/new
  GET /v1/workspaces
  GET /v1/workspace/:slug

## File: server/endpoints/api/admin/index.js

Function: apiAdminEndpoints

API Endpoints:
  GET /v1/admin/is-multi-user-mode
  GET /v1/admin/users
  POST /v1/admin/users/new
  POST /v1/admin/users/:id
  GET /v1/admin/invites
  POST /v1/admin/invite/new
  GET /v1/admin/preferences

## File: server/endpoints/api/document/index.js

Function: apiDocumentEndpoints
React Component: Collector
React Component: Collector
React Component: Collector

API Endpoints:
  GET /v1/documents
  GET /v1/document/:docName

## File: server/endpoints/api/system/index.js

Function: apiSystemEndpoints
React Component: VectorDb

API Endpoints:
  GET /v1/system/env-dump
  GET /v1/system
  GET /v1/system/vector-count

## File: server/endpoints/api/openai/index.js

Function: apiOpenAICompatibleEndpoints
React Component: LLMProvider
React Component: Embedder
React Component: VectorDBProvider

API Endpoints:
  GET /v1/openai/models

## File: server/endpoints/api/workspaceThread/index.js

Function: apiWorkspaceThreadEndpoints

## Directory: frontend/src/components

```
├── ChangeWarning
│   └── index.jsx
├── ChatBubble
│   └── index.jsx
├── ContextualSaveBar
│   └── index.jsx
├── DataConnectorOption
│   ├── index.jsx
│   └── media
│   │   ├── confluence.jpeg
│   │   ├── github.svg
│   │   ├── index.js
│   │   ├── link.svg
│   │   └── youtube.svg
├── DefaultChat
│   └── index.jsx
├── EditingChatBubble
│   └── index.jsx
├── EmbeddingSelection
│   ├── AzureAiOptions
│   │   └── index.jsx
│   ├── CohereOptions
│   │   └── index.jsx
│   ├── EmbedderItem
│   │   └── index.jsx
│   ├── GenericOpenAiOptions
│   │   └── index.jsx
│   ├── LMStudioOptions
│   │   └── index.jsx
│   ├── LiteLLMOptions
│   │   └── index.jsx
│   ├── LocalAiOptions
│   │   └── index.jsx
│   ├── NativeEmbeddingOptions
│   │   └── index.jsx
│   ├── OllamaOptions
│   │   └── index.jsx
│   ├── OpenAiOptions
│   │   └── index.jsx
│   └── VoyageAiOptions
│   │   └── index.jsx
├── Footer
│   └── index.jsx
├── LLMSelection
│   ├── AnthropicAiOptions
│   │   └── index.jsx
│   ├── AzureAiOptions
│   │   └── index.jsx
│   ├── CohereAiOptions
│   │   └── index.jsx
│   ├── GeminiLLMOptions
│   │   └── index.jsx
│   ├── GenericOpenAiOptions
│   │   └── index.jsx
│   ├── GroqAiOptions
│   │   └── index.jsx
│   ├── HuggingFaceOptions
│   │   └── index.jsx
│   ├── KoboldCPPOptions
│   │   └── index.jsx
│   ├── LLMItem
│   │   └── index.jsx
│   ├── LLMProviderOption
│   │   └── index.jsx
│   ├── LMStudioOptions
│   │   └── index.jsx
│   ├── LiteLLMOptions
│   │   └── index.jsx
│   ├── LocalAiOptions
│   │   └── index.jsx
│   ├── MistralOptions
│   │   └── index.jsx
│   ├── NativeLLMOptions
│   │   └── index.jsx
│   ├── OllamaLLMOptions
│   │   └── index.jsx
│   ├── OpenAiOptions
│   │   └── index.jsx
│   ├── OpenRouterOptions
│   │   └── index.jsx
│   ├── PerplexityOptions
│   │   └── index.jsx
│   ├── TextGenWebUIOptions
│   │   └── index.jsx
│   └── TogetherAiOptions
│   │   └── index.jsx
├── ModalWrapper
│   └── index.jsx
├── Modals
│   ├── DisplayRecoveryCodeModal
│   │   └── index.jsx
│   ├── ManageWorkspace
│   │   ├── DataConnectors
│   │   │   ├── ConnectorOption
│   │   │   │   └── index.jsx
│   │   │   ├── Connectors
│   │   │   │   ├── Confluence
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── Github
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── WebsiteDepth
│   │   │   │   │   └── index.jsx
│   │   │   │   └── Youtube
│   │   │   │   │   └── index.jsx
│   │   │   └── index.jsx
│   │   ├── Documents
│   │   │   ├── Directory
│   │   │   │   ├── FileRow
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── FolderRow
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── FolderSelectionPopup
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── MoveToFolderIcon.jsx
│   │   │   │   ├── NewFolderModal
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── index.jsx
│   │   │   │   └── utils.js
│   │   │   ├── UploadFile
│   │   │   │   ├── FileUploadProgress
│   │   │   │   │   └── index.jsx
│   │   │   │   └── index.jsx
│   │   │   ├── WorkspaceDirectory
│   │   │   │   ├── WorkspaceFileRow
│   │   │   │   │   └── index.jsx
│   │   │   │   └── index.jsx
│   │   │   └── index.jsx
│   │   └── index.jsx
│   ├── NewWorkspace.jsx
│   └── Password
│   │   ├── MultiUserAuth.jsx
│   │   ├── SingleUserAuth.jsx
│   │   └── index.jsx
├── Preloader.jsx
├── PrivateRoute
│   └── index.jsx
├── SettingsButton
│   └── index.jsx
├── SettingsSidebar
│   ├── MenuOption
│   │   └── index.jsx
│   └── index.jsx
├── Sidebar
│   ├── ActiveWorkspaces
│   │   ├── ThreadContainer
│   │   │   ├── ThreadItem
│   │   │   │   └── index.jsx
│   │   │   └── index.jsx
│   │   └── index.jsx
│   └── index.jsx
├── SpeechToText
│   └── BrowserNative
│   │   └── index.jsx
├── TextToSpeech
│   ├── BrowserNative
│   │   └── index.jsx
│   ├── ElevenLabsOptions
│   │   └── index.jsx
│   └── OpenAiOptions
│   │   └── index.jsx
├── TranscriptionSelection
│   ├── NativeTranscriptionOptions
│   │   └── index.jsx
│   └── OpenAiOptions
│   │   └── index.jsx
├── UserIcon
│   ├── index.jsx
│   └── workspace.png
├── UserMenu
│   ├── AccountModal
│   │   └── index.jsx
│   ├── UserButton
│   │   └── index.jsx
│   └── index.jsx
├── VectorDBSelection
│   ├── AstraDBOptions
│   │   └── index.jsx
│   ├── ChromaDBOptions
│   │   └── index.jsx
│   ├── LanceDBOptions
│   │   └── index.jsx
│   ├── MilvusDBOptions
│   │   └── index.jsx
│   ├── PineconeDBOptions
│   │   └── index.jsx
│   ├── QDrantDBOptions
│   │   └── index.jsx
│   ├── VectorDBItem
│   │   └── index.jsx
│   ├── WeaviateDBOptions
│   │   └── index.jsx
│   └── ZillizCloudOptions
│   │   └── index.jsx
├── WorkspaceChat
│   ├── ChatContainer
│   │   ├── ChatHistory
│   │   │   ├── Chartable
│   │   │   │   ├── CustomCell.jsx
│   │   │   │   ├── CustomTooltip.jsx
│   │   │   │   ├── chart-utils.js
│   │   │   │   └── index.jsx
│   │   │   ├── Citation
│   │   │   │   └── index.jsx
│   │   │   ├── HistoricalMessage
│   │   │   │   ├── Actions
│   │   │   │   │   ├── ActionMenu
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── DeleteMessage
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── EditMessage
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   ├── TTSButton
│   │   │   │   │   │   ├── asyncTts.jsx
│   │   │   │   │   │   ├── index.jsx
│   │   │   │   │   │   └── native.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   └── index.jsx
│   │   │   ├── PromptReply
│   │   │   │   └── index.jsx
│   │   │   └── index.jsx
│   │   ├── PromptInput
│   │   │   ├── AgentMenu
│   │   │   │   └── index.jsx
│   │   │   ├── SlashCommands
│   │   │   │   ├── SlashPresets
│   │   │   │   │   ├── AddPresetModal.jsx
│   │   │   │   │   ├── EditPresetModal.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   ├── endAgentSession.jsx
│   │   │   │   ├── icons
│   │   │   │   │   └── slash-commands-icon.svg
│   │   │   │   ├── index.jsx
│   │   │   │   └── reset.jsx
│   │   │   ├── SpeechToText
│   │   │   │   └── index.jsx
│   │   │   ├── StopGenerationButton
│   │   │   │   ├── index.jsx
│   │   │   │   └── stop.svg
│   │   │   ├── TextSizeMenu
│   │   │   │   └── index.jsx
│   │   │   └── index.jsx
│   │   └── index.jsx
│   ├── LoadingChat
│   │   └── index.jsx
│   └── index.jsx
└── lib
│   └── CTAButton
│   │   └── index.jsx
```



## File: frontend/src/components/Preloader.jsx

Function: PreLoader
Function: FullScreenLoader

## File: frontend/src/components/Sidebar/index.jsx

Function: Sidebar
Function: SidebarMobileHeader
Function: handleBg

## File: frontend/src/components/Sidebar/ActiveWorkspaces/index.jsx

Function: ActiveWorkspaces
Function: getWorkspaces

## File: frontend/src/components/Sidebar/ActiveWorkspaces/ThreadContainer/index.jsx

Function: ThreadContainer
Function: fetchThreads
Function: removeThread
Function: NewThreadButton
Function: DeleteAllThreadButton
Function: chatHandler
Function: handleKeyDown
Function: handleKeyUp
Function: toggleForDeletion
React Component: THREAD_RENAME_EVENT

## File: frontend/src/components/Sidebar/ActiveWorkspaces/ThreadContainer/ThreadItem/index.jsx

Function: ThreadItem
Function: OptionsMenu
Function: cleanupListeners
Function: setListeners
Function: outsideClick
Function: isEsc
React Component: THREAD_CALLOUT_DETAIL_WIDTH

## File: frontend/src/components/EmbeddingSelection/NativeEmbeddingOptions/index.jsx

Function: NativeEmbeddingOptions

## File: frontend/src/components/EmbeddingSelection/LMStudioOptions/index.jsx

Function: LMStudioEmbeddingOptions
Function: LMStudioModelSelection
Function: findCustomModels
Function: handleMaxChunkLengthChange

## File: frontend/src/components/EmbeddingSelection/GenericOpenAiOptions/index.jsx

Function: GenericOpenAiEmbeddingOptions

## File: frontend/src/components/EmbeddingSelection/LocalAiOptions/index.jsx

Function: LocalAiOptions
Function: LocalAIModelSelection
Function: findCustomModels

## File: frontend/src/components/EmbeddingSelection/OllamaOptions/index.jsx

Function: OllamaEmbeddingOptions
Function: OllamaEmbeddingModelSelection
Function: findCustomModels
Function: handleMaxChunkLengthChange

## File: frontend/src/components/EmbeddingSelection/LiteLLMOptions/index.jsx

Function: LiteLLMOptions
Function: LiteLLMModelSelection
Function: findCustomModels
Function: EmbeddingModelTooltip

## File: frontend/src/components/EmbeddingSelection/OpenAiOptions/index.jsx

Function: OpenAiOptions

## File: frontend/src/components/EmbeddingSelection/EmbedderItem/index.jsx

Function: EmbedderItem

## File: frontend/src/components/EmbeddingSelection/CohereOptions/index.jsx

Function: CohereEmbeddingOptions

## File: frontend/src/components/EmbeddingSelection/VoyageAiOptions/index.jsx

Function: VoyageAiOptions

## File: frontend/src/components/EmbeddingSelection/AzureAiOptions/index.jsx

Function: AzureAiOptions

## File: frontend/src/components/Footer/index.jsx

Function: Footer
Function: fetchFooterData
Function: ToolTipWrapper
React Component: MAX_ICONS
React Component: ICON_COMPONENTS

## File: frontend/src/components/ChatBubble/index.jsx

Function: ChatBubble

## File: frontend/src/components/ModalWrapper/index.jsx

Function: ModalWrapper

## File: frontend/src/components/SettingsButton/index.jsx

Function: SettingsButton

## File: frontend/src/components/Modals/NewWorkspace.jsx

Function: NewWorkspaceModal
Function: useNewWorkspaceModal
Function: noop
Function: showModal
Function: hideModal

## File: frontend/src/components/Modals/Password/MultiUserAuth.jsx

Function: MultiUserAuth
Function: RecoveryForm
Function: handleRecoveryCodeChange
Function: handleSubmit
Function: ResetPasswordForm
Function: handleSubmit
Function: handleDownloadComplete
Function: handleResetPassword
React Component: RecoveryForm
React Component: ResetPasswordForm

## File: frontend/src/components/Modals/Password/SingleUserAuth.jsx

Function: SingleUserAuth
Function: handleDownloadComplete

## File: frontend/src/components/Modals/Password/index.jsx

Function: PasswordModal
Function: usePasswordModal
Function: checkAuthReq

## File: frontend/src/components/Modals/DisplayRecoveryCodeModal/index.jsx

Function: RecoveryCodeModal
Function: downloadRecoveryCodes
Function: handleClose
Function: handleCopyToClipboard

## File: frontend/src/components/Modals/ManageWorkspace/index.jsx

Function: getSettings
Function: fetchWorkspace
Function: useManageWorkspaceModal
Function: noop
Function: ManageWorkspace
Function: ModalTabSwitcher
Function: showModal
Function: hideModal
React Component: ManageWorkspace
React Component: ModalTabSwitcher

## File: frontend/src/components/Modals/ManageWorkspace/DataConnectors/index.jsx

Function: DataConnectors
React Component: DATA_CONNECTORS

## File: frontend/src/components/Modals/ManageWorkspace/DataConnectors/Connectors/Youtube/index.jsx

Function: YoutubeOptions

## File: frontend/src/components/Modals/ManageWorkspace/DataConnectors/Connectors/Github/index.jsx

Function: GithubOptions
Function: GitHubBranchSelection
Function: fetchAllBranches
Function: PATAlert
Function: PATTooltip
React Component: DEFAULT_BRANCHES

## File: frontend/src/components/Modals/ManageWorkspace/DataConnectors/Connectors/Confluence/index.jsx

Function: ConfluenceOptions

## File: frontend/src/components/Modals/ManageWorkspace/DataConnectors/Connectors/WebsiteDepth/index.jsx

Function: WebsiteDepthOptions

## File: frontend/src/components/Modals/ManageWorkspace/DataConnectors/ConnectorOption/index.jsx

Function: ConnectorOption

## File: frontend/src/components/Modals/ManageWorkspace/Documents/index.jsx

Function: DocumentSettings
Function: fetchKeys
Function: moveSelectedItemsToWorkspace
React Component: MODEL_COSTS
React Component: COST_PER_TOKEN

## File: frontend/src/components/Modals/ManageWorkspace/Documents/Directory/MoveToFolderIcon.jsx

Function: MoveToFolderIcon

## File: frontend/src/components/Modals/ManageWorkspace/Documents/Directory/index.jsx

Function: Directory
Function: toggleSelection
Function: isSelected

## File: frontend/src/components/Modals/ManageWorkspace/Documents/Directory/utils.js

Function: filterFileSearchResults
Function: stripUuidAndJsonFromString
React Component: LEVENSHTEIN_MIN

## File: frontend/src/components/Modals/ManageWorkspace/Documents/Directory/FileRow/index.jsx

Function: FileRow

## File: frontend/src/components/Modals/ManageWorkspace/Documents/Directory/FolderSelectionPopup/index.jsx

Function: FolderSelectionPopup
Function: handleFolderSelect

## File: frontend/src/components/Modals/ManageWorkspace/Documents/Directory/FolderRow/index.jsx

Function: FolderRow
Function: handleExpandClick

## File: frontend/src/components/Modals/ManageWorkspace/Documents/Directory/NewFolderModal/index.jsx

Function: NewFolderModal

## File: frontend/src/components/Modals/ManageWorkspace/Documents/WorkspaceDirectory/index.jsx

Function: WorkspaceDirectory
Function: dismissAlert
Function: handlePinEvent
Function: dismissAlert
Function: handlePinEvent
React Component: PinAlert
React Component: DocumentWatchAlert

## File: frontend/src/components/Modals/ManageWorkspace/Documents/WorkspaceDirectory/WorkspaceFileRow/index.jsx

Function: WorkspaceFileRow
Function: RemoveItemFromWorkspace
React Component: PinItemToWorkspace
React Component: WatchForChanges
React Component: RemoveItemFromWorkspace

## File: frontend/src/components/Modals/ManageWorkspace/Documents/UploadFile/index.jsx

Function: UploadFile
Function: checkProcessorOnline
Function: handleUploadError

## File: frontend/src/components/Modals/ManageWorkspace/Documents/UploadFile/FileUploadProgress/index.jsx

Function: FileUploadProgressComponent
Function: uploadFile
Function: fadeOut
Function: beginFadeOut

## File: frontend/src/components/SettingsSidebar/index.jsx

Function: SettingsSidebar
Function: handleBg
Function: SupportEmail
Function: HoldToReveal
Function: SidebarOptions
Function: onPress
Function: onRelease
React Component: SidebarOptions

## File: frontend/src/components/SettingsSidebar/MenuOption/index.jsx

Function: MenuOption
Function: useIsExpanded
Function: hasVisibleOptions
Function: isVisible
Function: generateStorageKey
Function: handleClick

## File: frontend/src/components/ContextualSaveBar/index.jsx

Function: ContextualSaveBar

## File: frontend/src/components/SpeechToText/BrowserNative/index.jsx

Function: BrowserNative

## File: frontend/src/components/DefaultChat/index.jsx

Function: DefaultChatContainer
Function: processMsgs
React Component: MESSAGES

## File: frontend/src/components/PrivateRoute/index.jsx

Function: useIsAuthenticated
Function: AdminRoute
Function: ManagerRoute
Function: PrivateRoute

## File: frontend/src/components/UserMenu/index.jsx

Function: UserMenu

## File: frontend/src/components/UserMenu/UserButton/index.jsx

Function: UserButton
Function: UserDisplay
Function: handleClose
Function: handleOpenAccountModal

## File: frontend/src/components/UserMenu/AccountModal/index.jsx

Function: AccountModal
Function: LanguagePreference

## File: frontend/src/components/DataConnectorOption/index.jsx

Function: DataConnectorOption

## File: frontend/src/components/DataConnectorOption/media/index.js

React Component: ConnectorImages

## File: frontend/src/components/LLMSelection/LLMItem/index.jsx

Function: LLMItem

## File: frontend/src/components/LLMSelection/MistralOptions/index.jsx

Function: MistralOptions
Function: MistralModelSelection
Function: findCustomModels

## File: frontend/src/components/LLMSelection/TextGenWebUIOptions/index.jsx

Function: TextGenWebUIOptions

## File: frontend/src/components/LLMSelection/LMStudioOptions/index.jsx

Function: LMStudioOptions
Function: LMStudioModelSelection
Function: findCustomModels
Function: handleMaxTokensChange

## File: frontend/src/components/LLMSelection/HuggingFaceOptions/index.jsx

Function: HuggingFaceOptions

## File: frontend/src/components/LLMSelection/GenericOpenAiOptions/index.jsx

Function: GenericOpenAiOptions

## File: frontend/src/components/LLMSelection/OpenRouterOptions/index.jsx

Function: OpenRouterOptions
Function: OpenRouterModelSelection
Function: findCustomModels

## File: frontend/src/components/LLMSelection/LocalAiOptions/index.jsx

Function: LocalAiOptions
Function: LocalAIModelSelection
Function: findCustomModels

## File: frontend/src/components/LLMSelection/LLMProviderOption/index.jsx

Function: LLMProviderOption

## File: frontend/src/components/LLMSelection/GeminiLLMOptions/index.jsx

Function: GeminiLLMOptions

## File: frontend/src/components/LLMSelection/GroqAiOptions/index.jsx

Function: GroqAiOptions

## File: frontend/src/components/LLMSelection/AnthropicAiOptions/index.jsx

Function: AnthropicAiOptions

## File: frontend/src/components/LLMSelection/OllamaLLMOptions/index.jsx

Function: OllamaLLMOptions
Function: OllamaLLMModelSelection
Function: findCustomModels
Function: handleMaxTokensChange

## File: frontend/src/components/LLMSelection/CohereAiOptions/index.jsx

Function: CohereAiOptions

## File: frontend/src/components/LLMSelection/LiteLLMOptions/index.jsx

Function: LiteLLMOptions
Function: LiteLLMModelSelection
Function: findCustomModels

## File: frontend/src/components/LLMSelection/OpenAiOptions/index.jsx

Function: OpenAiOptions
Function: OpenAIModelSelection
Function: findCustomModels

## File: frontend/src/components/LLMSelection/PerplexityOptions/index.jsx

Function: PerplexityOptions
Function: PerplexityModelSelection
Function: findCustomModels

## File: frontend/src/components/LLMSelection/KoboldCPPOptions/index.jsx

Function: KoboldCPPOptions
Function: KoboldCPPModelSelection
Function: findCustomModels
Function: handleTokenLimitChange

## File: frontend/src/components/LLMSelection/TogetherAiOptions/index.jsx

Function: TogetherAiOptions
Function: TogetherAiModelSelection
Function: findCustomModels

## File: frontend/src/components/LLMSelection/NativeLLMOptions/index.jsx

Function: NativeLLMOptions
Function: NativeModelSelection
Function: findCustomModels

## File: frontend/src/components/LLMSelection/AzureAiOptions/index.jsx

Function: AzureAiOptions

## File: frontend/src/components/TranscriptionSelection/NativeTranscriptionOptions/index.jsx

Function: NativeTranscriptionOptions
Function: LocalWarning
Function: WhisperSmall
Function: WhisperLarge

## File: frontend/src/components/TranscriptionSelection/OpenAiOptions/index.jsx

Function: OpenAiWhisperOptions

## File: frontend/src/components/lib/CTAButton/index.jsx

Function: CTAButton

## File: frontend/src/components/TextToSpeech/ElevenLabsOptions/index.jsx

Function: ElevenLabsOptions
Function: ElevenLabsModelSelection
Function: findCustomModels

## File: frontend/src/components/TextToSpeech/OpenAiOptions/index.jsx

Function: toProperCase
Function: OpenAiTextToSpeechOptions

## File: frontend/src/components/TextToSpeech/BrowserNative/index.jsx

Function: BrowserNative

## File: frontend/src/components/ChangeWarning/index.jsx

Function: ChangeWarningModal

## File: frontend/src/components/WorkspaceChat/index.jsx

Function: WorkspaceChat
Function: getHistory
Function: copyCodeSnippet
Function: setEventDelegatorForCodeSnippets

## File: frontend/src/components/WorkspaceChat/LoadingChat/index.jsx

Function: LoadingChat

## File: frontend/src/components/WorkspaceChat/ChatContainer/index.jsx

Function: ChatContainer
Function: setMessageEmit
Function: fetchReply
Function: handleWSS
Function: handleMessageChange
Function: regenerateAssistantMessage

## File: frontend/src/components/WorkspaceChat/ChatContainer/ChatHistory/index.jsx

Function: ChatHistory
Function: watchScrollEvent
Function: StatusResponse
Function: WorkspaceChatSuggestions
Function: getTextSizeClass
Function: handleTextSizeChange
Function: handleScroll
Function: scrollToBottom
Function: handleSendSuggestedMessage

## File: frontend/src/components/WorkspaceChat/ChatContainer/ChatHistory/Citation/index.jsx

Function: combineLikeSources
Function: Citations
Function: SkeletonLine
Function: omitChunkHeader
Function: CitationDetailModal
Function: parseChunkSource
Function: ConfluenceIcon
React Component: Citation
React Component: CitationIcon
React Component: ConfluenceIcon
React Component: ICONS

## File: frontend/src/components/WorkspaceChat/ChatContainer/ChatHistory/PromptReply/index.jsx

Function: WorkspaceProfileImage
Function: PromptReply
React Component: PromptReply

## File: frontend/src/components/WorkspaceChat/ChatContainer/ChatHistory/Chartable/CustomTooltip.jsx

Function: invertColor
Function: padZero
Function: Tooltip

## File: frontend/src/components/WorkspaceChat/ChatContainer/ChatHistory/Chartable/chart-utils.js

Function: getTremorColor
React Component: Colors

## File: frontend/src/components/WorkspaceChat/ChatContainer/ChatHistory/Chartable/index.jsx

Function: Chartable
Function: DownloadGraph
Function: dataFormatter
Function: renderChart
Function: customTooltip

## File: frontend/src/components/WorkspaceChat/ChatContainer/ChatHistory/Chartable/CustomCell.jsx

Function: CustomCell

## File: frontend/src/components/WorkspaceChat/ChatContainer/ChatHistory/HistoricalMessage/index.jsx

Function: ProfileImage
Function: adjustTextArea
React Component: DOMPurify
React Component: HistoricalMessage

## File: frontend/src/components/WorkspaceChat/ChatContainer/ChatHistory/HistoricalMessage/Actions/index.jsx

Function: FeedbackButton
Function: CopyMessage
Function: RegenerateMessage
Function: Actions
React Component: Actions

## File: frontend/src/components/WorkspaceChat/ChatContainer/ChatHistory/HistoricalMessage/Actions/TTSButton/asyncTts.jsx

Function: AsyncTTSMessage
Function: speakMessage
Function: setupPlayer

## File: frontend/src/components/WorkspaceChat/ChatContainer/ChatHistory/HistoricalMessage/Actions/TTSButton/index.jsx

Function: TTSMessage
Function: getSettings

## File: frontend/src/components/WorkspaceChat/ChatContainer/ChatHistory/HistoricalMessage/Actions/TTSButton/native.jsx

Function: NativeTTSMessage
Function: endSpeechUtterance
Function: speakMessage

## File: frontend/src/components/WorkspaceChat/ChatContainer/ChatHistory/HistoricalMessage/Actions/DeleteMessage/index.jsx

Function: useWatchDeleteMessage
Function: listenForEvent
Function: onEndAnimation
Function: onDeleteEvent
Function: DeleteMessage
Function: emitDeleteEvent
React Component: DELETE_EVENT

## File: frontend/src/components/WorkspaceChat/ChatContainer/ChatHistory/HistoricalMessage/Actions/ActionMenu/index.jsx

Function: ActionMenu
Function: toggleMenu
Function: handleFork
Function: handleDelete
Function: handleClickOutside

## File: frontend/src/components/WorkspaceChat/ChatContainer/ChatHistory/HistoricalMessage/Actions/EditMessage/index.jsx

Function: useEditMessage
Function: onEditEvent
Function: listenForEdits
Function: EditMessageAction
Function: handleEditClick
Function: EditMessageForm
Function: handleSaveMessage
Function: cancelEdits
React Component: EDIT_EVENT

## File: frontend/src/components/WorkspaceChat/ChatContainer/PromptInput/index.jsx

Function: PromptInput
Function: handlePromptUpdate
Function: handleSubmit
Function: resetTextAreaHeight
Function: checkForSlash
Function: checkForAt
Function: captureEnter
Function: adjustTextArea
React Component: PROMPT_INPUT_EVENT

## File: frontend/src/components/WorkspaceChat/ChatContainer/PromptInput/TextSizeMenu/index.jsx

Function: TextSizeButton
Function: TextSizeMenu
Function: listenForOutsideClick
Function: closeIfOutside
Function: handleTextSizeChange

## File: frontend/src/components/WorkspaceChat/ChatContainer/PromptInput/StopGenerationButton/index.jsx

Function: StopGenerationButton
Function: emitHaltEvent

## File: frontend/src/components/WorkspaceChat/ChatContainer/PromptInput/SpeechToText/index.jsx

Function: SpeechToText
Function: startSTTSession
Function: endTTSSession
React Component: SILENCE_INTERVAL

## File: frontend/src/components/WorkspaceChat/ChatContainer/PromptInput/SlashCommands/endAgentSession.jsx

Function: EndAgentSession

## File: frontend/src/components/WorkspaceChat/ChatContainer/PromptInput/SlashCommands/index.jsx

Function: SlashCommandsButton
Function: SlashCommands
Function: listenForOutsideClick
Function: useSlashCommands
Function: closeIfOutside

## File: frontend/src/components/WorkspaceChat/ChatContainer/PromptInput/SlashCommands/reset.jsx

Function: ResetCommand

## File: frontend/src/components/WorkspaceChat/ChatContainer/PromptInput/SlashCommands/SlashPresets/AddPresetModal.jsx

Function: AddPresetModal
Function: handleCommandChange

## File: frontend/src/components/WorkspaceChat/ChatContainer/PromptInput/SlashCommands/SlashPresets/index.jsx

Function: SlashPresets
Function: handleEditPreset
React Component: CMD_REGEX

## File: frontend/src/components/WorkspaceChat/ChatContainer/PromptInput/SlashCommands/SlashPresets/EditPresetModal.jsx

Function: EditPresetModal
Function: handleSubmit
Function: handleCommandChange

## File: frontend/src/components/WorkspaceChat/ChatContainer/PromptInput/AgentMenu/index.jsx

Function: AvailableAgentsButton
Function: AbilityTag
Function: AvailableAgents
Function: listenForOutsideClick
Function: useAvailableAgents
Function: FirstTimeAgentUser
Function: firstTimeShow
Function: closeIfOutside
Function: dismiss
React Component: SEEN_FT_AGENT_MODAL

## File: frontend/src/components/VectorDBSelection/QDrantDBOptions/index.jsx

Function: QDrantDBOptions

## File: frontend/src/components/VectorDBSelection/ZillizCloudOptions/index.jsx

Function: ZillizCloudOptions

## File: frontend/src/components/VectorDBSelection/ChromaDBOptions/index.jsx

Function: ChromaDBOptions

## File: frontend/src/components/VectorDBSelection/PineconeDBOptions/index.jsx

Function: PineconeDBOptions

## File: frontend/src/components/VectorDBSelection/VectorDBItem/index.jsx

Function: VectorDBItem

## File: frontend/src/components/VectorDBSelection/MilvusDBOptions/index.jsx

Function: MilvusDBOptions

## File: frontend/src/components/VectorDBSelection/AstraDBOptions/index.jsx

Function: AstraDBOptions

## File: frontend/src/components/VectorDBSelection/LanceDBOptions/index.jsx

Function: LanceDBOptions

## File: frontend/src/components/VectorDBSelection/WeaviateDBOptions/index.jsx

Function: WeaviateDBOptions

## File: frontend/src/components/EditingChatBubble/index.jsx

Function: EditingChatBubble

## File: frontend/src/components/UserIcon/index.jsx

Function: UserIcon
Function: toPseudoRandomInteger

## Directory: frontend/src/pages

```
├── 404.jsx
├── Admin
│   ├── Agents
│   │   ├── Badges
│   │   │   └── default.jsx
│   │   ├── DefaultSkillPanel
│   │   │   └── index.jsx
│   │   ├── GenericSkillPanel
│   │   │   └── index.jsx
│   │   ├── SQLConnectorSelection
│   │   │   ├── DBConnection.jsx
│   │   │   ├── NewConnectionModal.jsx
│   │   │   ├── icons
│   │   │   │   ├── mssql.png
│   │   │   │   ├── mysql.png
│   │   │   │   └── postgresql.png
│   │   │   └── index.jsx
│   │   ├── WebSearchSelection
│   │   │   ├── SearchProviderItem
│   │   │   │   └── index.jsx
│   │   │   ├── SearchProviderOptions
│   │   │   │   └── index.jsx
│   │   │   ├── icons
│   │   │   │   ├── bing.png
│   │   │   │   ├── google.png
│   │   │   │   ├── searxng.png
│   │   │   │   ├── serper.png
│   │   │   │   └── serply.png
│   │   │   └── index.jsx
│   │   ├── index.jsx
│   │   └── skills.js
│   ├── ExperimentalFeatures
│   │   ├── Features
│   │   │   └── LiveSync
│   │   │   │   ├── manage
│   │   │   │   │   ├── DocumentSyncQueueRow
│   │   │   │   │   │   └── index.jsx
│   │   │   │   │   └── index.jsx
│   │   │   │   └── toggle.jsx
│   │   ├── features.js
│   │   └── index.jsx
│   ├── Invitations
│   │   ├── InviteRow
│   │   │   └── index.jsx
│   │   ├── NewInviteModal
│   │   │   └── index.jsx
│   │   └── index.jsx
│   ├── Logging
│   │   ├── LogRow
│   │   │   └── index.jsx
│   │   └── index.jsx
│   ├── System
│   │   └── index.jsx
│   ├── Users
│   │   ├── NewUserModal
│   │   │   └── index.jsx
│   │   ├── UserRow
│   │   │   ├── EditUserModal
│   │   │   │   └── index.jsx
│   │   │   └── index.jsx
│   │   └── index.jsx
│   └── Workspaces
│   │   ├── NewWorkspaceModal
│   │   │   └── index.jsx
│   │   ├── WorkspaceRow
│   │   │   └── index.jsx
│   │   └── index.jsx
├── GeneralSettings
│   ├── ApiKeys
│   │   ├── ApiKeyRow
│   │   │   └── index.jsx
│   │   ├── NewApiKeyModal
│   │   │   └── index.jsx
│   │   └── index.jsx
│   ├── Appearance
│   │   ├── CustomAppName
│   │   │   └── index.jsx
│   │   ├── CustomLogo
│   │   │   └── index.jsx
│   │   ├── CustomMessages
│   │   │   └── index.jsx
│   │   ├── CustomSiteSettings
│   │   │   └── index.jsx
│   │   ├── FooterCustomization
│   │   │   ├── NewIconForm
│   │   │   │   └── index.jsx
│   │   │   └── index.jsx
│   │   ├── LanguagePreference
│   │   │   └── index.jsx
│   │   ├── SupportEmail
│   │   │   └── index.jsx
│   │   └── index.jsx
│   ├── AudioPreference
│   │   ├── index.jsx
│   │   ├── stt.jsx
│   │   └── tts.jsx
│   ├── Chats
│   │   ├── ChatRow
│   │   │   └── index.jsx
│   │   └── index.jsx
│   ├── EmbedChats
│   │   ├── ChatRow
│   │   │   └── index.jsx
│   │   └── index.jsx
│   ├── EmbedConfigs
│   │   ├── EmbedRow
│   │   │   ├── CodeSnippetModal
│   │   │   │   └── index.jsx
│   │   │   ├── EditEmbedModal
│   │   │   │   └── index.jsx
│   │   │   └── index.jsx
│   │   ├── NewEmbedModal
│   │   │   └── index.jsx
│   │   └── index.jsx
│   ├── EmbeddingPreference
│   │   └── index.jsx
│   ├── EmbeddingTextSplitterPreference
│   │   └── index.jsx
│   ├── LLMPreference
│   │   └── index.jsx
│   ├── PrivacyAndData
│   │   └── index.jsx
│   ├── Security
│   │   └── index.jsx
│   ├── TranscriptionPreference
│   │   └── index.jsx
│   └── VectorDatabase
│   │   └── index.jsx
├── Invite
│   ├── NewUserModal
│   │   └── index.jsx
│   └── index.jsx
├── Login
│   └── index.jsx
├── Main
│   └── index.jsx
├── OnboardingFlow
│   ├── Steps
│   │   ├── CreateWorkspace
│   │   │   └── index.jsx
│   │   ├── DataHandling
│   │   │   └── index.jsx
│   │   ├── Home
│   │   │   ├── index.jsx
│   │   │   ├── l_group.png
│   │   │   └── r_group.png
│   │   ├── LLMPreference
│   │   │   └── index.jsx
│   │   ├── Survey
│   │   │   └── index.jsx
│   │   ├── UserSetup
│   │   │   └── index.jsx
│   │   └── index.jsx
│   └── index.jsx
├── WorkspaceChat
│   └── index.jsx
└── WorkspaceSettings
│   ├── AgentConfig
│   │   ├── AgentLLMSelection
│   │   │   ├── AgentLLMItem
│   │   │   │   └── index.jsx
│   │   │   └── index.jsx
│   │   ├── AgentModelSelection
│   │   │   └── index.jsx
│   │   └── index.jsx
│   ├── ChatSettings
│   │   ├── ChatHistorySettings
│   │   │   └── index.jsx
│   │   ├── ChatModeSelection
│   │   │   └── index.jsx
│   │   ├── ChatPromptSettings
│   │   │   └── index.jsx
│   │   ├── ChatQueryRefusalResponse
│   │   │   └── index.jsx
│   │   ├── ChatTemperatureSettings
│   │   │   └── index.jsx
│   │   ├── WorkspaceLLMSelection
│   │   │   ├── ChatModelSelection
│   │   │   │   └── index.jsx
│   │   │   ├── WorkspaceLLMItem
│   │   │   │   └── index.jsx
│   │   │   └── index.jsx
│   │   └── index.jsx
│   ├── GeneralAppearance
│   │   ├── DeleteWorkspace
│   │   │   └── index.jsx
│   │   ├── SuggestedChatMessages
│   │   │   └── index.jsx
│   │   ├── WorkspaceName
│   │   │   └── index.jsx
│   │   ├── WorkspacePfp
│   │   │   └── index.jsx
│   │   └── index.jsx
│   ├── Members
│   │   ├── AddMemberModal
│   │   │   └── index.jsx
│   │   ├── WorkspaceMemberRow
│   │   │   └── index.jsx
│   │   └── index.jsx
│   ├── VectorDatabase
│   │   ├── DocumentSimilarityThreshold
│   │   │   └── index.jsx
│   │   ├── MaxContextSnippets
│   │   │   └── index.jsx
│   │   ├── ResetDatabase
│   │   │   └── index.jsx
│   │   ├── VectorCount
│   │   │   └── index.jsx
│   │   ├── VectorDBIdentifier
│   │   │   └── index.jsx
│   │   └── index.jsx
│   └── index.jsx
```



## File: frontend/src/pages/404.jsx

Function: Contact

## File: frontend/src/pages/GeneralSettings/EmbeddingPreference/index.jsx

Function: GeneralEmbeddingPreference
Function: embedderModelChanged
Function: fetchKeys
Function: updateChoice
Function: handleXButton
React Component: EMBEDDERS

## File: frontend/src/pages/GeneralSettings/PrivacyAndData/index.jsx

Function: PrivacyAndDataHandling
Function: fetchSettings
Function: ThirdParty
Function: TelemetryLogs
Function: toggleTelemetry

## File: frontend/src/pages/GeneralSettings/TranscriptionPreference/index.jsx

Function: TranscriptionModelPreference
Function: fetchKeys
Function: updateProviderChoice
Function: handleXButton
React Component: PROVIDERS

## File: frontend/src/pages/GeneralSettings/EmbedChats/index.jsx

Function: EmbedChats
Function: ChatsContainer
Function: fetchChats
Function: handlePrevious
Function: handleNext
Function: handleDeleteChat

## File: frontend/src/pages/GeneralSettings/EmbedChats/ChatRow/index.jsx

Function: ChatRow
Function: TextPreview
Function: ConnectionDetails
React Component: TextPreview
React Component: ConnectionDetails

## File: frontend/src/pages/GeneralSettings/Security/index.jsx

Function: GeneralSecurity
Function: MultiUserMode
Function: fetchIsMultiUserMode
Function: PasswordProtection
Function: fetchIsMultiUserMode
React Component: PW_REGEX

## File: frontend/src/pages/GeneralSettings/AudioPreference/stt.jsx

Function: SpeechToTextProvider
Function: updateProviderChoice
Function: handleXButton
React Component: PROVIDERS

## File: frontend/src/pages/GeneralSettings/AudioPreference/index.jsx

Function: AudioPreference
Function: fetchKeys

## File: frontend/src/pages/GeneralSettings/AudioPreference/tts.jsx

Function: TextToSpeechProvider
Function: updateProviderChoice
Function: handleXButton
React Component: PROVIDERS

## File: frontend/src/pages/GeneralSettings/Appearance/index.jsx

Function: Appearance

## File: frontend/src/pages/GeneralSettings/Appearance/LanguagePreference/index.jsx

Function: LanguagePreference

## File: frontend/src/pages/GeneralSettings/Appearance/FooterCustomization/index.jsx

Function: FooterCustomization
Function: fetchFooterIcons
Function: handleRemoveIcon

## File: frontend/src/pages/GeneralSettings/Appearance/FooterCustomization/NewIconForm/index.jsx

Function: NewIconForm
Function: handleClickOutside
Function: handleSubmit
Function: handleRemove
Function: handleIconChange
Function: handleUrlChange

## File: frontend/src/pages/GeneralSettings/Appearance/SupportEmail/index.jsx

Function: SupportEmail
Function: handleChange

## File: frontend/src/pages/GeneralSettings/Appearance/CustomAppName/index.jsx

Function: CustomAppName
Function: handleChange

## File: frontend/src/pages/GeneralSettings/Appearance/CustomMessages/index.jsx

Function: CustomMessages
Function: fetchMessages
Function: addMessage
Function: removeMessage
Function: handleMessageChange

## File: frontend/src/pages/GeneralSettings/Appearance/CustomSiteSettings/index.jsx

Function: CustomSiteSettings
Function: handleSiteSettingUpdate

## File: frontend/src/pages/GeneralSettings/Appearance/CustomLogo/index.jsx

Function: CustomLogo
Function: logoInit
Function: triggerFileInputClick

## File: frontend/src/pages/GeneralSettings/ApiKeys/index.jsx

Function: AdminApiKeys
Function: ApiKeysContainer
Function: fetchExistingKeys
React Component: Model

## File: frontend/src/pages/GeneralSettings/ApiKeys/ApiKeyRow/index.jsx

Function: ApiKeyRow
Function: resetStatus
Function: copyApiKey
React Component: Model

## File: frontend/src/pages/GeneralSettings/ApiKeys/NewApiKeyModal/index.jsx

Function: NewApiKeyModal
Function: resetStatus
Function: copyApiKey
React Component: Model

## File: frontend/src/pages/GeneralSettings/EmbeddingTextSplitterPreference/index.jsx

Function: isNullOrNaN
Function: EmbeddingTextSplitterPreference
Function: fetchSettings

## File: frontend/src/pages/GeneralSettings/VectorDatabase/index.jsx

Function: GeneralVectorDatabase
Function: fetchKeys
Function: updateVectorChoice
Function: handleXButton
React Component: VECTOR_DBS

## File: frontend/src/pages/GeneralSettings/LLMPreference/index.jsx

Function: GeneralLLMPreference
Function: fetchKeys
Function: updateLLMChoice
Function: handleXButton
React Component: AVAILABLE_LLM_PROVIDERS

## File: frontend/src/pages/GeneralSettings/Chats/index.jsx

Function: WorkspaceChats
Function: handleClickOutside
Function: fetchChats
Function: ChatsContainer
Function: toggleMenu
Function: handlePrevious
Function: handleNext

## File: frontend/src/pages/GeneralSettings/Chats/ChatRow/index.jsx

Function: ChatRow
Function: TextPreview
React Component: TextPreview

## File: frontend/src/pages/GeneralSettings/EmbedConfigs/index.jsx

Function: EmbedConfigs
Function: EmbedContainer
Function: fetchUsers

## File: frontend/src/pages/GeneralSettings/EmbedConfigs/EmbedRow/index.jsx

Function: EmbedRow
Function: ActiveDomains

## File: frontend/src/pages/GeneralSettings/EmbedConfigs/EmbedRow/EditEmbedModal/index.jsx

Function: EditEmbedModal

## File: frontend/src/pages/GeneralSettings/EmbedConfigs/EmbedRow/CodeSnippetModal/index.jsx

Function: CodeSnippetModal
Function: createScriptTagSnippet
Function: like
Function: ScriptTag
Function: handleClick
React Component: ScriptTag

## File: frontend/src/pages/GeneralSettings/EmbedConfigs/NewEmbedModal/index.jsx

Function: enforceSubmissionSchema
Function: NewEmbedModal
Function: fetchWorkspaces
Function: WorkspaceSelection
Function: ChatModeSelection
Function: PermittedDomains
Function: handleChange
Function: NumberInput
Function: BooleanInput
React Component: WorkspaceSelection
React Component: ChatModeSelection
React Component: PermittedDomains
React Component: NumberInput
React Component: BooleanInput

## File: frontend/src/pages/OnboardingFlow/index.jsx

Function: OnboardingFlow
React Component: StepPage

## File: frontend/src/pages/OnboardingFlow/Steps/index.jsx

Function: OnboardingLayout
React Component: OnboardingSteps

## File: frontend/src/pages/OnboardingFlow/Steps/Home/index.jsx

Function: OnboardingHome

## File: frontend/src/pages/OnboardingFlow/Steps/UserSetup/index.jsx

Function: UserSetup
Function: handleForward
Function: handleBack
Function: handleYes
Function: handleNo
Function: JustMe
Function: setNewPassword
Function: MyTeam
Function: setNewUsername
Function: setNewPassword
React Component: TITLE
React Component: DESCRIPTION
React Component: JustMe
React Component: MyTeam

## File: frontend/src/pages/OnboardingFlow/Steps/CreateWorkspace/index.jsx

Function: CreateWorkspace
Function: handleForward
Function: handleBack
React Component: TITLE
React Component: DESCRIPTION

## File: frontend/src/pages/OnboardingFlow/Steps/LLMPreference/index.jsx

Function: LLMPreference
Function: fetchKeys
Function: handleForward
Function: handleBack
React Component: TITLE
React Component: DESCRIPTION
React Component: LLMS

## File: frontend/src/pages/OnboardingFlow/Steps/DataHandling/index.jsx

Function: DataHandling
Function: fetchKeys
Function: handleForward
Function: handleBack
React Component: TITLE
React Component: DESCRIPTION
React Component: LLM_SELECTION_PRIVACY
React Component: VECTOR_DB_PRIVACY
React Component: EMBEDDING_ENGINE_PRIVACY

## File: frontend/src/pages/OnboardingFlow/Steps/Survey/index.jsx

Function: sendQuestionnaire
Function: Survey
Function: handleForward
Function: skipSurvey
Function: handleBack
React Component: TITLE
React Component: DESCRIPTION

## File: frontend/src/pages/Admin/ExperimentalFeatures/features.js



## File: frontend/src/pages/Admin/ExperimentalFeatures/index.jsx

Function: ExperimentalFeatures
Function: fetchSettings
Function: FeatureLayout
Function: FeatureList
Function: SelectedFeatureComponent
Function: FeatureVerification
Function: acceptTos
React Component: Component

## File: frontend/src/pages/Admin/ExperimentalFeatures/Features/LiveSync/toggle.jsx

Function: LiveSyncToggle
Function: toggleFeatureFlag

## File: frontend/src/pages/Admin/ExperimentalFeatures/Features/LiveSync/manage/index.jsx

Function: LiveDocumentSyncManager
Function: WatchedDocumentsContainer
Function: fetchData

## File: frontend/src/pages/Admin/ExperimentalFeatures/Features/LiveSync/manage/DocumentSyncQueueRow/index.jsx

Function: DocumentSyncQueueRow

## File: frontend/src/pages/Admin/Agents/skills.js



## File: frontend/src/pages/Admin/Agents/index.jsx

Function: AdminAgents
Function: fetchSettings
Function: SkillLayout
Function: SkillList
Function: handleBeforeUnload
Function: toggleAgentSkill
React Component: SelectedSkillComponent

## File: frontend/src/pages/Admin/Agents/DefaultSkillPanel/index.jsx

Function: DefaultSkillPanel

## File: frontend/src/pages/Admin/Agents/WebSearchSelection/index.jsx

Function: AgentWebSearchSelection
Function: updateChoice
Function: handleXButton
React Component: SEARCH_PROVIDERS

## File: frontend/src/pages/Admin/Agents/WebSearchSelection/SearchProviderItem/index.jsx

Function: SearchProviderItem

## File: frontend/src/pages/Admin/Agents/WebSearchSelection/SearchProviderOptions/index.jsx

Function: GoogleSearchOptions
Function: SerperDotDevOptions
Function: BingSearchOptions
Function: SerplySearchOptions
Function: SearXNGOptions

## File: frontend/src/pages/Admin/Agents/SQLConnectorSelection/NewConnectionModal.jsx

Function: assembleConnectionString
Function: NewSQLConnection
Function: handleClose
Function: onFormChange
Function: handleUpdate
Function: DBEngine
React Component: DEFAULT_ENGINE
React Component: DEFAULT_CONFIG

## File: frontend/src/pages/Admin/Agents/SQLConnectorSelection/index.jsx

Function: AgentSQLConnectorSelection

## File: frontend/src/pages/Admin/Agents/SQLConnectorSelection/DBConnection.jsx

Function: DBConnection
Function: removeConfirmation
React Component: DB_LOGOS

## File: frontend/src/pages/Admin/Agents/GenericSkillPanel/index.jsx

Function: GenericSkillPanel

## File: frontend/src/pages/Admin/Agents/Badges/default.jsx

Function: DefaultBadge

## File: frontend/src/pages/Admin/Workspaces/index.jsx

Function: AdminWorkspaces
Function: WorkspacesContainer
Function: fetchData

## File: frontend/src/pages/Admin/Workspaces/WorkspaceRow/index.jsx

Function: WorkspaceRow

## File: frontend/src/pages/Admin/Workspaces/NewWorkspaceModal/index.jsx

Function: NewWorkspaceModal

## File: frontend/src/pages/Admin/System/index.jsx

Function: AdminSystem
Function: fetchSettings

## File: frontend/src/pages/Admin/Users/index.jsx

Function: AdminUsers
Function: UsersContainer
Function: fetchUsers
Function: RoleHintDisplay
React Component: ROLE_HINT

## File: frontend/src/pages/Admin/Users/NewUserModal/index.jsx

Function: NewUserModal

## File: frontend/src/pages/Admin/Users/UserRow/index.jsx

Function: UserRow
React Component: ModMap

## File: frontend/src/pages/Admin/Users/UserRow/EditUserModal/index.jsx

Function: EditUserModal

## File: frontend/src/pages/Admin/Logging/index.jsx

Function: AdminLogs
Function: fetchLogs
Function: LogsContainer
Function: handlePrevious
Function: handleNext

## File: frontend/src/pages/Admin/Logging/LogRow/index.jsx

Function: LogRow
Function: parseAndSetMetadata
Function: handleRowClick
Function: EventMetadata
Function: EventBadge
React Component: EventMetadata
React Component: EventBadge

## File: frontend/src/pages/Admin/Invitations/index.jsx

Function: AdminInvites
Function: InvitationsContainer
Function: fetchInvites

## File: frontend/src/pages/Admin/Invitations/NewInviteModal/index.jsx

Function: NewInviteModal
Function: resetStatus
Function: fetchWorkspaces
Function: WorkspaceOption
Function: copyInviteLink
Function: handleWorkspaceSelection

## File: frontend/src/pages/Admin/Invitations/InviteRow/index.jsx

Function: InviteRow
Function: resetStatus
Function: copyInviteLink

## File: frontend/src/pages/Invite/index.jsx

Function: InvitePage
Function: checkInvite

## File: frontend/src/pages/Invite/NewUserModal/index.jsx

Function: NewUserModal

## File: frontend/src/pages/WorkspaceSettings/index.jsx

Function: WorkspaceSettings
Function: ShowWorkspaceChat
Function: getWorkspace
Function: TabItem
React Component: TABS
React Component: TabContent

## File: frontend/src/pages/WorkspaceSettings/ChatSettings/index.jsx

Function: ChatSettings
Function: fetchSettings

## File: frontend/src/pages/WorkspaceSettings/ChatSettings/ChatModeSelection/index.jsx

Function: ChatModeSelection

## File: frontend/src/pages/WorkspaceSettings/ChatSettings/ChatTemperatureSettings/index.jsx

Function: recommendedSettings
Function: ChatTemperatureSettings

## File: frontend/src/pages/WorkspaceSettings/ChatSettings/WorkspaceLLMSelection/index.jsx

Function: WorkspaceLLMSelection
Function: updateLLMChoice
Function: handleXButton
React Component: NO_MODEL_SELECTION
React Component: DISABLED_PROVIDERS
React Component: LLM_DEFAULT
React Component: LLMS

## File: frontend/src/pages/WorkspaceSettings/ChatSettings/WorkspaceLLMSelection/ChatModelSelection/index.jsx

Function: ChatModelSelection

## File: frontend/src/pages/WorkspaceSettings/ChatSettings/WorkspaceLLMSelection/WorkspaceLLMItem/index.jsx

Function: WorkspaceLLM
Function: handleProviderSelection
Function: SetupProvider
Function: handleUpdate
React Component: LLMOption

## File: frontend/src/pages/WorkspaceSettings/ChatSettings/ChatQueryRefusalResponse/index.jsx

Function: ChatQueryRefusalResponse

## File: frontend/src/pages/WorkspaceSettings/ChatSettings/ChatHistorySettings/index.jsx

Function: ChatHistorySettings

## File: frontend/src/pages/WorkspaceSettings/ChatSettings/ChatPromptSettings/index.jsx

Function: ChatPromptSettings

## File: frontend/src/pages/WorkspaceSettings/GeneralAppearance/index.jsx

Function: GeneralInfo
Function: fetchWorkspace

## File: frontend/src/pages/WorkspaceSettings/GeneralAppearance/SuggestedChatMessages/index.jsx

Function: SuggestedChatMessages
Function: fetchWorkspace
Function: addMessage
Function: removeMessage
Function: startEditing
Function: handleRemoveMessage
Function: onEditChange

## File: frontend/src/pages/WorkspaceSettings/GeneralAppearance/WorkspaceName/index.jsx

Function: WorkspaceName

## File: frontend/src/pages/WorkspaceSettings/GeneralAppearance/DeleteWorkspace/index.jsx

Function: DeleteWorkspace

## File: frontend/src/pages/WorkspaceSettings/GeneralAppearance/WorkspacePfp/index.jsx

Function: WorkspacePfp
Function: fetchWorkspace

## File: frontend/src/pages/WorkspaceSettings/AgentConfig/index.jsx

Function: WorkspaceAgentConfiguration
Function: fetchSettings
Function: LoadingSkeleton

## File: frontend/src/pages/WorkspaceSettings/AgentConfig/AgentModelSelection/index.jsx

Function: calling
Function: supportedModel
Function: AgentModelSelection

## File: frontend/src/pages/WorkspaceSettings/AgentConfig/AgentLLMSelection/index.jsx

Function: AgentLLMSelection
Function: updateLLMChoice
Function: handleXButton
React Component: ENABLED_PROVIDERS
React Component: WARN_PERFORMANCE
React Component: LLM_DEFAULT
React Component: LLMS

## File: frontend/src/pages/WorkspaceSettings/AgentConfig/AgentLLMSelection/AgentLLMItem/index.jsx

Function: WorkspaceLLM
Function: handleProviderSelection
Function: SetupProvider
Function: handleUpdate
React Component: LLMOption

## File: frontend/src/pages/WorkspaceSettings/VectorDatabase/index.jsx

Function: VectorDatabase

## File: frontend/src/pages/WorkspaceSettings/VectorDatabase/VectorDBIdentifier/index.jsx

Function: VectorDBIdentifier

## File: frontend/src/pages/WorkspaceSettings/VectorDatabase/VectorCount/index.jsx

Function: VectorCount
Function: fetchVectorCount

## File: frontend/src/pages/WorkspaceSettings/VectorDatabase/MaxContextSnippets/index.jsx

Function: MaxContextSnippets

## File: frontend/src/pages/WorkspaceSettings/VectorDatabase/ResetDatabase/index.jsx

Function: ResetDatabase

## File: frontend/src/pages/WorkspaceSettings/VectorDatabase/DocumentSimilarityThreshold/index.jsx

Function: DocumentSimilarityThreshold

## File: frontend/src/pages/WorkspaceSettings/Members/index.jsx

Function: Members
Function: fetchData

## File: frontend/src/pages/WorkspaceSettings/Members/WorkspaceMemberRow/index.jsx

Function: WorkspaceMemberRow

## File: frontend/src/pages/WorkspaceSettings/Members/AddMemberModal/index.jsx

Function: AddMemberModal
Function: handleUserSelect
Function: handleSelectAll
Function: handleUnselect
Function: isUserSelected
Function: handleSearch

## File: frontend/src/pages/WorkspaceChat/index.jsx

Function: WorkspaceChat
Function: ShowWorkspaceChat
Function: getWorkspace

## File: frontend/src/pages/Main/index.jsx

Function: Main

## File: frontend/src/pages/Login/index.jsx

Function: Login

## Directory: collector/utils

```
├── EncryptionWorker
│   └── index.js
├── WhisperProviders
│   ├── OpenAiWhisper.js
│   └── localWhisper.js
├── comKey
│   └── index.js
├── constants.js
├── extensions
│   ├── Confluence
│   │   ├── ConfluenceLoader
│   │   │   └── index.js
│   │   └── index.js
│   ├── GithubRepo
│   │   ├── RepoLoader
│   │   │   └── index.js
│   │   └── index.js
│   ├── WebsiteDepth
│   │   └── index.js
│   └── YoutubeTranscript
│   │   ├── YoutubeLoader
│   │   │   ├── index.js
│   │   │   └── youtube-transcript.js
│   │   └── index.js
├── files
│   ├── index.js
│   └── mime.js
├── http
│   └── index.js
├── logger
│   └── index.js
├── tokenizer
│   └── index.js
└── url
│   └── index.js
```



## File: collector/utils/constants.js

React Component: WATCH_DIRECTORY
React Component: ACCEPTED_MIMES
React Component: SUPPORTED_FILETYPE_CONVERTERS

## File: collector/utils/EncryptionWorker/index.js

Class: on
Class: EncryptionWorker

## File: collector/utils/logger/index.js

Function: formatArgs
Function: setLogger
Class: Logger

## File: collector/utils/tokenizer/index.js

Function: tokenizeString

## File: collector/utils/url/index.js

Function: isInvalidIp
Function: validURL
React Component: VALID_PROTOCOLS
React Component: INVALID_OCTETS
React Component: IPRegex

## File: collector/utils/extensions/YoutubeTranscript/index.js

Function: validYoutubeVideoUrl
Function: fetchVideoTranscriptContent
Function: loadYouTubeTranscript
React Component: UrlPattern

## File: collector/utils/extensions/YoutubeTranscript/YoutubeLoader/index.js

Class: YoutubeLoader
Class: from

## File: collector/utils/extensions/YoutubeTranscript/YoutubeLoader/youtube-transcript.js

Class: YoutubeTranscriptError
Class: YoutubeTranscript
React Component: RE_YOUTUBE
React Component: USER_AGENT

## File: collector/utils/extensions/Confluence/index.js

Function: loadConfluence
Function: fetchConfluencePage
Function: generateAPIBaseUrl
Function: validSpaceUrl
Function: generateChunkSource
React Component: UrlPattern

## File: collector/utils/extensions/Confluence/ConfluenceLoader/index.js

Function: extractCodeBlocks
Class: ConfluencePagesLoader

## File: collector/utils/extensions/GithubRepo/index.js

Function: loadGithubRepo
Function: fetchGithubFile
Function: generateChunkSource
React Component: RepoLoader

## File: collector/utils/extensions/GithubRepo/RepoLoader/index.js

Class: RepoLoader
React Component: UrlPattern

## File: collector/utils/extensions/WebsiteDepth/index.js

Function: discoverLinks
Function: getPageLinks
Function: extractLinks
Function: bulkScrapePages
Function: websiteScraper

## File: collector/utils/comKey/index.js

Class: CommunicationKey
Class: does

## File: collector/utils/WhisperProviders/OpenAiWhisper.js

Class: OpenAiWhisper

## File: collector/utils/WhisperProviders/localWhisper.js

Function: pipeline
Class: LocalWhisper
React Component: SCALING_FACTOR

## File: collector/utils/http/index.js

Function: reqBody
Function: queryParams

## File: collector/utils/files/mime.js

Class: MimeDetector
React Component: MimeLib

## File: collector/utils/files/index.js

Function: isTextType
Function: trashFile
Function: createdDate
Function: writeToServerDocuments
Function: wipeCollectorStorage
Function: isWithin
Function: normalizePath
Function: sanitizeFileName