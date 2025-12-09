# CLAUDE.md - Repository Guide for AI Assistants

## Repository Overview

This is a Python-based data science and game development repository containing two primary Streamlit applications:

1. **Data Prediction App** (`open.py`) - A machine learning web application for CSV data analysis and prediction
2. **Reversi Game** (`riversi.ipynb`) - A Google Colab notebook implementing the classic Othello/Reversi board game

**Primary Language**: Python 3.11
**Main Framework**: Streamlit
**Development Environment**: VS Code Dev Containers / GitHub Codespaces

---

## Codebase Structure

```
/home/user/TEST/
├── .devcontainer/
│   └── devcontainer.json          # Dev container configuration
├── .git/                          # Git repository metadata
├── IMG.JPG                        # Background/reference image for data prediction app
├── open.py                        # Main data prediction Streamlit application
├── riversi.ipynb                  # Reversi game Jupyter notebook (Colab-ready)
└── requirements.txt               # Python dependencies
```

### Key Files

#### `open.py` (Data Prediction App)
- **Purpose**: CSV-based machine learning prediction tool
- **Features**:
  - File upload interface for CSV data
  - Correlation analysis visualization
  - Automated algorithm selection (Linear Regression, SVR, Random Forest)
  - Predictive modeling with accuracy reporting
  - Result export to CSV with downloadable link
- **Key Dependencies**: streamlit, pandas, numpy, scikit-learn, PIL
- **Expected CSV Format**:
  - Column 1: Target variable (value to predict)
  - Columns 2+: Feature variables (predictors)
  - Last rows with empty Column 1 values will be predicted

#### `riversi.ipynb` (Reversi Game Notebook)
- **Purpose**: Runnable Reversi game for Google Colab
- **Features**:
  - Complete Reversi/Othello game logic
  - Streamlit-based UI with visual game board
  - Background image support (`game.jpg`)
  - Ngrok tunneling for public access
  - Auto-restart mechanism (kills previous processes)
- **Platform**: Google Colab (contains Colab-specific commands)
- **Note**: Contains hardcoded ngrok authtoken placeholder ("PATH") that needs user configuration

#### `.devcontainer/devcontainer.json`
- **Base Image**: `mcr.microsoft.com/devcontainers/python:1-3.11-bookworm`
- **Auto-Opens**: `README.md`, `open.py` (Note: README.md doesn't exist yet)
- **Extensions**: Python extension pack (ms-python.python, ms-python.vscode-pylance)
- **Startup Command**: `streamlit run open.py --server.enableCORS false --server.enableXsrfProtection false`
- **Port**: 8501 (auto-forwarded, opens in preview)
- **Package Installation**: Auto-installs from `requirements.txt` + streamlit

---

## Technology Stack

### Core Technologies
- **Python 3.11**: Primary programming language
- **Streamlit**: Web application framework for both projects
- **scikit-learn**: Machine learning algorithms (Linear Regression, SVR, Random Forest)
- **pandas**: Data manipulation and CSV handling
- **numpy**: Numerical computing
- **PIL (Pillow)**: Image processing

### Development Tools
- **VS Code Dev Containers**: Containerized development environment
- **GitHub Codespaces**: Cloud-based development
- **Jupyter Notebooks**: For Colab integration
- **pyngrok**: Public tunnel creation (notebook only)

---

## Development Workflows

### Local Development Setup

1. **Container Environment** (Recommended):
   ```bash
   # Open in VS Code with Dev Containers extension
   # Container automatically installs dependencies and starts Streamlit
   ```

2. **Manual Setup**:
   ```bash
   pip install -r requirements.txt
   streamlit run open.py --server.enableCORS false --server.enableXsrfProtection false
   ```

3. **Access Application**:
   - Local: `http://localhost:8501`
   - Codespaces: Auto-forwarded port with preview

### Running the Reversi Game

1. Open `riversi.ipynb` in Google Colab
2. Update ngrok authtoken (line with `authtoken = "PATH"`)
3. Upload `game.jpg` background image to Colab environment
4. Run all cells sequentially
5. Access via generated ngrok URL

### Testing Workflow

**No formal test suite currently exists**. When implementing tests:
- Use `pytest` for unit tests
- Test ML model accuracy with known datasets
- Validate Reversi game logic with standard opening positions
- Test CSV parsing with various formats

---

## Code Conventions

### Python Style
- **Encoding**: SHIFT-JIS for CSV files (Japanese character support)
- **Comments**: Mixed Japanese and English
- **Naming Conventions**:
  - Functions: `snake_case` (e.g., `set_bg_image`, `get_flippable_stones`)
  - Variables: `snake_case` (e.g., `uploaded_file`, `x_train`)
  - Constants: `UPPER_SNAKE_CASE` (e.g., `BOARDW`, `TYPE_BLACK`)

### Streamlit Patterns
- Use `st.session_state` for game state management (Reversi)
- Employ `st.empty()` for dynamic status messages
- Utilize `st.button()` with unique keys for interactive elements
- Apply custom CSS via `st.markdown()` with `unsafe_allow_html=True`

### Machine Learning Conventions
- **Train/Test Split**: 70/30 ratio (test_size=0.3, random_state=1)
- **Algorithm Selection**: Automatic based on test score (A1, A2, A3 comparison)
- **Accuracy Reporting**: Rounded up to nearest integer percentage
- **Result Precision**: 2 decimal places for predictions

### Data Handling
- Drop NaN rows before model training (`df.dropna()`)
- Use `.iloc` for positional indexing
- First column always represents target variable
- Base64 encoding for CSV downloads

---

## Git Workflow

### Branch Naming Convention
- **Feature branches**: Must start with `claude/` prefix
- **Current branch**: `claude/claude-md-miy101ganrf2q2ei-017TkSFi4rVfwC64BcSkepHR`
- **Naming pattern**: `claude/<descriptive-name>-<session-id>`

### Commit Guidelines
1. Write clear, descriptive commit messages in English
2. Use conventional commit format when appropriate:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation
   - `refactor:` for code restructuring
3. Commit frequency: Atomic commits preferred (one logical change per commit)

### Push Requirements
- Always use: `git push -u origin <branch-name>`
- Branch must start with `claude/` and include session ID
- Retry on network failures (up to 4 times with exponential backoff)

### Recent Commits
- `4746f15`: Added Dev Container Folder
- `1e67260`, `fabff36`: Colab notebook creation
- `16926d4`: File uploads

---

## Dependencies Management

### requirements.txt
```
streamlit
Pillow
scikit-learn
```

### Additional Dependencies (Not in requirements.txt)
- `pandas` (typically included with scikit-learn)
- `numpy` (scikit-learn dependency)
- `pyngrok` (notebook only, installed via `!pip install`)

### Updating Dependencies
```bash
# Add new dependency
echo "package_name" >> requirements.txt

# Container will auto-install on rebuild
# Or manually install:
pip install -r requirements.txt
```

---

## Common Tasks for AI Assistants

### When Modifying `open.py`

1. **Adding New ML Algorithms**:
   - Import from scikit-learn
   - Add model training between lines 66-79
   - Update comparison logic (lines 82-93)
   - Maintain scoring variable naming pattern (A1, A2, A3, etc.)

2. **Changing CSV Format**:
   - Update documentation (lines 19-20)
   - Modify iloc slicing logic if column positions change
   - Ensure SHIFT-JIS encoding maintained for Japanese support

3. **UI Modifications**:
   - Preserve existing session state patterns
   - Maintain button uniqueness with `key` parameter
   - Keep status messages in `comment.write()` pattern

### When Modifying `riversi.ipynb`

1. **Game Logic Changes**:
   - Update within `app_code` string (lines starting with `app_code = """`)
   - Maintain board representation (bytearray of size BOARDW * BOARDW)
   - Preserve turn/pass/endgame logic flow

2. **UI Customization**:
   - Modify CSS within `set_bg_image()` function
   - Update piece representations (⚫, ⚪) if needed
   - Adjust color schemes in style block

3. **Deployment Changes**:
   - Update ngrok token handling
   - Modify port if not using 8501
   - Adjust process cleanup commands if needed

### Adding New Features

1. **New Streamlit App**:
   ```bash
   # Create new Python file
   # Update devcontainer.json to auto-open it
   # Add to requirements.txt if new dependencies needed
   # Document in this CLAUDE.md
   ```

2. **New Notebook**:
   - Follow riversi.ipynb pattern
   - Include Colab badge in first cell
   - Document required setup steps
   - Add file upload cells for dependencies

### Code Quality Checks

Before committing:
1. Ensure no hardcoded secrets (check ngrok tokens, API keys)
2. Verify SHIFT-JIS encoding for CSV operations
3. Test Streamlit apps load without errors
4. Validate notebook runs in Colab environment
5. Update this CLAUDE.md if architecture changes

---

## Known Issues and Limitations

1. **Missing README.md**: Dev container references non-existent README.md file
2. **Hardcoded Paths**: `riversi.ipynb` expects `/content/game.jpg` (Colab path)
3. **Ngrok Token**: Placeholder "PATH" requires manual configuration
4. **No Tests**: No automated test suite implemented
5. **Mixed Languages**: Comments mix Japanese and English
6. **IMG.JPG Dependency**: `open.py` requires IMG.JPG file in root directory
7. **CSV Encoding**: Hardcoded to SHIFT-JIS, may fail with UTF-8 CSVs
8. **ML Model Persistence**: Models not saved; retrained on each prediction run
9. **Error Handling**: Limited error handling in prediction pipeline
10. **Reversi Bugs**: Several bugs in riversi.ipynb:
    - Line defining `black_count` is duplicated (should be `white_count` on second instance)
    - Win condition checks use `black_count` vs `black_count` (always false)

---

## Best Practices for AI Assistants

### DO:
- Read existing files before modifying them
- Preserve SHIFT-JIS encoding for CSV operations
- Maintain session state patterns in Streamlit apps
- Update this CLAUDE.md when making architectural changes
- Test changes in dev container environment
- Use descriptive commit messages
- Ask for clarification on ngrok token or deployment specifics

### DON'T:
- Remove or modify IMG.JPG without updating open.py
- Change CSV column expectations without updating documentation
- Break Streamlit session state management
- Commit secrets or API tokens
- Modify git config without permission
- Force push to main/master branches
- Skip dependency updates in requirements.txt

### Security Considerations:
- Never commit ngrok authtokens or API keys
- Validate CSV file uploads to prevent code injection
- Be cautious with `unsafe_allow_html=True` usage
- Sanitize user inputs before ML model training
- Review base64 encoding/decoding for vulnerabilities

---

## Troubleshooting Guide

### Issue: Streamlit Won't Start
- Check port 8501 availability
- Verify requirements.txt installed
- Review startup logs in container
- Ensure `open.py` has no syntax errors

### Issue: CSV Upload Fails
- Verify SHIFT-JIS encoding
- Check CSV has required format (target in column 1)
- Ensure no completely empty rows
- Validate numeric data types

### Issue: ML Prediction Error
- Confirm sufficient training data (minimum rows)
- Check for non-numeric values in feature columns
- Verify no infinite/NaN values after dropna()
- Ensure test/train split has enough samples

### Issue: Reversi Game Won't Load in Colab
- Upload `game.jpg` to Colab files
- Update ngrok authtoken
- Check streamlit and pyngrok installation
- Verify previous processes killed successfully

### Issue: Dev Container Won't Build
- Check Docker daemon running
- Verify internet connection for image pull
- Review devcontainer.json syntax
- Check VS Code Dev Containers extension installed

---

## Future Improvement Suggestions

1. **Testing**:
   - Add pytest suite for open.py
   - Unit tests for Reversi game logic
   - Integration tests for ML pipeline

2. **Documentation**:
   - Create README.md with user-facing documentation
   - Add docstrings to functions
   - Include example CSV files

3. **Code Quality**:
   - Fix Reversi game bugs (white_count variable, win conditions)
   - Add error handling to ML pipeline
   - Implement input validation
   - Remove hardcoded paths

4. **Features**:
   - Model persistence/caching
   - Support for UTF-8 CSVs
   - Configuration file for ngrok/deployment settings
   - Multiple background image support

5. **DevOps**:
   - Add pre-commit hooks
   - Implement CI/CD pipeline
   - Create deployment scripts
   - Add logging infrastructure

---

## Contact and Support

- **Repository Issues**: Use GitHub issue tracker
- **Dev Container Problems**: Check VS Code Dev Containers documentation
- **Streamlit Questions**: Refer to https://docs.streamlit.io
- **ML Algorithm Details**: See scikit-learn documentation

---

**Last Updated**: 2025-12-09
**Repository State**: Clean working directory on branch `claude/claude-md-miy101ganrf2q2ei-017TkSFi4rVfwC64BcSkepHR`
**Primary Maintainer**: AI Assistant (Claude Code)
