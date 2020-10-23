# sklearn-api

Sklearn API makes it easy to take an arbitrary trained 
sklearn model and deploy it as a web API.  This makes depolyment of models 
simpler for production environments that are able to interact with APIs.

To get the web API running, run the following in your terminal:

```bash
python main.py
```

Here is an example of how users interact with the API.
```python
import pandas as pd
from user import ModelAPI

# Create a ModelAPI object to interact with the API
model = ModelAPI(api_url = 'http://127.0.0.1:5000/')

# Make a prediction
df = pd.DataFrame({'A': [3, 6, 7], 
                   'B': [9, 4, 3]})
df['y'] = model.predict(df[['A', 'B']])
```

