# Contributing to RagOverflow

Thank you for your interest in contributing to RagOverflow! We are happy to accept contributions from the community to help improve this project.

## How to Contribute

### 1. Fork & Clone the Repo
```bash
git clone https://github.com/DunnyBunny1/ragoverflow.git
cd ragoverflow
```

2. Set up Your Environment

Follow the instructions in the [README](README.md) to get the project running with Docker.

Ensure both the frontend (Streamlit) and backend (Flask) containers are running locally before making changes.

3. Create Your Feature Branch

```bash
git checkout -b <my_new_feature_branch>
```

4. Make Changes
- Follow the existing code style and conventions.
- If you’re adding new functionality, make sure to document it.
- Ensure that your changes work with the existing Docker setup and that the app behaves as expected.

5. Update the Changelog

- If you’ve made any significant changes, such as adding new features or fixing bugs, please update the [CHANGELOG.md](CHANGELOG.md) file.

Follow the format used in the changelog. Example:
```
## 0.0.1
### Added
- New feature to query technical forums for programming answers.
- Docker Compose setup for easier local development.

### Fixed
- Resolved issue where the Flask backend wasn't properly connecting to PineconeDB.
```

6. Commit & Push Your Changes
```bash
git commit -m "feature: decsription of changes made" 
git push --set-upstream origin/my-new-feature
```
7. Open a Pull Request
- Go to your fork and click on "New Pull Request."
- Clearly describe the changes you've made and why they are beneficial.
- Link any related issues in the PR description.

## Code Style Guidelines

- Python: Follow PEP8 and use type hints where possible.

- Frontend (Streamlit): Maintain consistency in UI layout and component usage. Keep the interface clean and minimal.

- Docker: Ensure both the frontend and backend work well together in Docker containers.

- Testing: Add or update tests as necessary. If you've updated any API functionality, ensure it’s covered with appropriate test cases.

## Questions? 
If you have any questions or need clarification, please open an issue or contact the maintainers. We appreciate your contributions to RagOverflow!