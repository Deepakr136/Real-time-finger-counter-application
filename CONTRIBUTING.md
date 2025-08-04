# Contributing to Real-Time Finger Counter

Thank you for your interest in contributing to this project! We welcome contributions from everyone.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/yourusername/finger-counter/issues)
2. If not, create a new issue with:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version, etc.)

### Suggesting Features

1. Check existing issues for similar feature requests
2. Create a new issue with:
   - Clear description of the feature
   - Use case and benefits
   - Possible implementation approach

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Commit with clear messages**
   ```bash
   git commit -m "Add: new feature description"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/finger-counter.git
   cd finger-counter
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Test the application:
   ```bash
   python demo.py  # Test core functionality
   streamlit run app.py  # Test full application
   ```

## Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and small

## Testing

Before submitting a PR:

1. Test on different Python versions (3.8+)
2. Verify webcam functionality works
3. Check that the interface is responsive
4. Test edge cases (no webcam, poor lighting, etc.)

## Areas for Contribution

- **Performance optimization**
- **UI/UX improvements**
- **Additional detection algorithms**
- **Mobile device support**
- **Accessibility features**
- **Documentation improvements**
- **Bug fixes**

## Questions?

Feel free to open an issue for any questions about contributing!