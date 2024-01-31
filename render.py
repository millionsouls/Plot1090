import time
import requests

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

table = pq.read_table('./data.parquet')
table.to_pandas()
