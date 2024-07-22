# Databricks notebook source
import os
os.environ["DATABRICKS_INSTANCE"] = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiUrl().get()
os.environ["DATABRICKS_TOKEN"] = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()

# COMMAND ----------

# MAGIC %sh 
# MAGIC curl -s -X GET -H "Authorization: Bearer $DATABRICKS_TOKEN" $DATABRICKS_INSTANCE/api/2.0/workspace/list -d '{"path": "/Workspace/Users/scott.bauersfeld@databricks.com/wsfssynctesting/tttt"}'

# COMMAND ----------

# MAGIC %sh 
# MAGIC curl -s -X GET -H "Authorization: Bearer $DATABRICKS_TOKEN" $DATABRICKS_INSTANCE/api/2.0/workspace/list -d '{"path": "/Workspace/Users/scott.bauersfeld@databricks.com/wsfssynctesting/tttt", "use_qualified_names": true}'

# COMMAND ----------

# MAGIC %sh 
# MAGIC curl -s -X GET -H "Authorization: Bearer $DATABRICKS_TOKEN" $DATABRICKS_INSTANCE/api/2.0/workspace/get-status -d '{"path": "/Workspace/Users/scott.bauersfeld@databricks.com/wsfssynctesting/tttt/foo"}'

# COMMAND ----------

# MAGIC %sh 
# MAGIC curl -s -X GET -H "Authorization: Bearer $DATABRICKS_TOKEN" $DATABRICKS_INSTANCE/api/2.0/workspace/get-status -d '{"path": "/Workspace/Users/scott.bauersfeld@databricks.com/wsfssynctesting/tttt/foo.py"}'

# COMMAND ----------

# MAGIC %sh 
# MAGIC curl -s -X GET -H "Authorization: Bearer $DATABRICKS_TOKEN" $DATABRICKS_INSTANCE/api/2.0/workspace/get-status -d '{"path": "/Workspace/Users/scott.bauersfeld@databricks.com/wsfssynctesting/tttt/foo", "use_qualified_names": "true"}'

# COMMAND ----------

# MAGIC %sh 
# MAGIC curl -s -X GET -H "Authorization: Bearer $DATABRICKS_TOKEN" $DATABRICKS_INSTANCE/api/2.0/workspace/get-status -d '{"path": "/Workspace/Users/scott.bauersfeld@databricks.com/wsfssynctesting/tttt/foo.py", "use_qualified_names": "true"}'

# COMMAND ----------


