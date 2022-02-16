# Energy Management System (EMS)
A python library containing the EMS solution deployment.

### Installation
Install using virtual environment:
```
pip install ems/dist/ems-0.1.0-py3-none-any.whl
```

### Get started
Datasets can be obtained by running:
```Python
from ems import Datasets
Datasets.list()
```
Savings calculations can be obtained by running:
```Python
from ems import Savings
Savings.get()
```
Ad-hoc analysis are :
```Python
from ems import Analysis
Analysis.list()
Analysis.get('AhuExp')
```

Install using virtual environment pip install ems/dist/ems-0.1.0-py3-none-any.whl