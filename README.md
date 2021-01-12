# django CMS 4 Migration

## When do I need this package?
This package is designed to migrate a django CMS 3.5+ project to django CMS 4.0.

## What does this package do?
- Keeps any draft and published content, ensuring that any new draft changes are kept as a new draft version in djangocms_versioning. 

## Limitations
Due to the nature of the changes between django CMS 3.5+ and 4.0 the package will fail to function if an incompatible package is installed. 

This may require you to:
 - Fork or copy and modify this package to work with any bespoke requirements your project has (we may accept these changes back for popular packages as a configurable option)
 - Ensure that all installed packages for your project are 

## Prerequisites 
Require knowledge of the changes and new features in 4.0:
- New cms app configuration
- Revised Page, Title (Now named PageContent) and Placeholder relationships

Requires knowledge of django CMS Versioning
- Grouper and content model terms
- Understanding how versioning selects published content

### Install the following packages
The following packages are not yet officially released, they need to be installed directly from the repository. We need your help to make packages v4.0 compatible and to provide documentation for the wider community!

django CMS 4.0
```
pip install http://github.com/divio/django-cms/tarball/release/4.0.x#egg=django-cms
```

djangocms-text-ckeditor
```
pip install https://github.com/divio/djangocms-text-ckeditor/tarball/support/4.0.x#egg=djangocms-text-ckeditor
```

djangocms-versioning
```
pip install https://github.com/divio/djangocms-versioning/tarball/master#egg=djangocms-versioning
```

djangocms-alias
```
pip install https://github.com/divio/djangocms-alias/tarball/master#egg=djangocms-alias
```

## Installation
**Warning**: This package can leave your DB in a corrupted state if used incorrectly, be sure to backup any databases prior to running any commands listed here!

First install this package in your project
```
pip install djangocms-4-migration
```

## Running
Simply run the following command to run the data migration. 
**Note:** This command calls the django migrate command, this is because it has to run commands that save information that would have been lost by running the cms migrations directly.
```
python manage.py cms4_migration
```

## Common solutions for django CMS 4.0 compatibility

Import PageContent in a backwards compatible way (Title).
```python

# django CMS v4
try:
    from cms.models import PageContent
# django CMS 3.x
except ImportError:
    from cms.models import Title as PageContent
```
