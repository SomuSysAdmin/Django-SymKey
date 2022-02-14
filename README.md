# Usage
To get the password for a specific credential, use:

```python
s.credential_set.filter(tag='<your_tag>').first().password
```
