{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c3fd4211",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3\n",
    "import pandas as pd\n",
    "\n",
    "# Connect to database\n",
    "conn = sqlite3.connect(\"C:\\\\Git1\\\\Python_homework\\\\lesson-17\\\\data\\\\chinook.db\")\n",
    "\n",
    "# Load tables\n",
    "customers = pd.read_sql(\"SELECT * FROM customers\", conn)\n",
    "invoices = pd.read_sql(\"SELECT * FROM invoices\", conn)\n",
    "\n",
    "# Inner join\n",
    "cust_invoices = customers.merge(\n",
    "    invoices,\n",
    "    on=\"CustomerId\",\n",
    "    how=\"inner\"\n",
    ")\n",
    "\n",
    "# Total number of invoices per customer\n",
    "invoice_counts = (\n",
    "    cust_invoices\n",
    "    .groupby(\"CustomerId\")\n",
    "    .size()\n",
    "    .reset_index(name=\"Total_Invoices\")\n",
    ")\n",
    "\n",
    "invoice_counts\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
