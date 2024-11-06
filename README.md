# Siwar API

[![PyPI version](https://badge.fury.io/py/siwar-api.svg)](https://badge.fury.io/py/siwar-api)
[![Python Package](https://github.com/osama-ata/siwar-api/actions/workflows/python-package.yml/badge.svg)](https://github.com/osama-ata/siwar-api/actions/workflows/python-package.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python wrapper for the Siwar Arabic Lexicon API (siwar.ksaa.gov.sa). This library provides easy access to Arabic lexical data, word meanings, roots, patterns, and morphological information.


## Installation

```bash
pip install siwar-api
```

## Quick Start

- Obtian an [API key](https://siwar.ksaa.gov.sa/developers).

```python
from siwar import SiwarClient

# Initialize client
client = SiwarClient(api_key='your-api-key')

# Search public entries
results = client.search_public('محرك')

# Get lexicon information
lexicons = client.get_public_lexicons()

# Get word details
senses = client.get_entry_senses('محرك')
conjugations = client.get_entry_conjugations('محرك')
```

## Features

- Complete coverage of Siwar API endpoints
- Support for both public and private lexicon access
- Rich Arabic language processing utilities
- Type hints for better IDE support
- Comprehensive error handling
- Detailed documentation

## Documentation

For full documentation and examples, visit our [GitHub Wiki](https://github.com/osama-ata/siwar-api/wiki).

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Siwar Arabic Lexicon](https://siwar.ksaa.gov.sa) for providing the API
- All our [contributors](CONTRIBUTORS.md)
- [API documentaion](https://siwar.ksaa.gov.sa/api-external)

## Support

If you encounter any problems or have suggestions, please [open an issue](https://github.com/osama-ata/siwar-api/issues/new/choose).
