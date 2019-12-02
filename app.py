{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: flask_sqlalchemy in ./anaconda3/lib/python3.7/site-packages (2.4.1)\n",
      "Requirement already satisfied: SQLAlchemy>=0.8.0 in ./anaconda3/lib/python3.7/site-packages (from flask_sqlalchemy) (1.3.5)\n",
      "Requirement already satisfied: Flask>=0.10 in ./anaconda3/lib/python3.7/site-packages (from flask_sqlalchemy) (1.1.1)\n",
      "Requirement already satisfied: Jinja2>=2.10.1 in ./anaconda3/lib/python3.7/site-packages (from Flask>=0.10->flask_sqlalchemy) (2.10.1)\n",
      "Requirement already satisfied: Werkzeug>=0.15 in ./anaconda3/lib/python3.7/site-packages (from Flask>=0.10->flask_sqlalchemy) (0.15.4)\n",
      "Requirement already satisfied: itsdangerous>=0.24 in ./anaconda3/lib/python3.7/site-packages (from Flask>=0.10->flask_sqlalchemy) (1.1.0)\n",
      "Requirement already satisfied: click>=5.1 in ./anaconda3/lib/python3.7/site-packages (from Flask>=0.10->flask_sqlalchemy) (7.0)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in ./anaconda3/lib/python3.7/site-packages (from Jinja2>=2.10.1->Flask>=0.10->flask_sqlalchemy) (1.1.1)\n",
      "Requirement already satisfied: flask_heroku in ./anaconda3/lib/python3.7/site-packages (0.1.9)\n",
      "Requirement already satisfied: Flask in ./anaconda3/lib/python3.7/site-packages (from flask_heroku) (1.1.1)\n",
      "Requirement already satisfied: Jinja2>=2.10.1 in ./anaconda3/lib/python3.7/site-packages (from Flask->flask_heroku) (2.10.1)\n",
      "Requirement already satisfied: Werkzeug>=0.15 in ./anaconda3/lib/python3.7/site-packages (from Flask->flask_heroku) (0.15.4)\n",
      "Requirement already satisfied: click>=5.1 in ./anaconda3/lib/python3.7/site-packages (from Flask->flask_heroku) (7.0)\n",
      "Requirement already satisfied: itsdangerous>=0.24 in ./anaconda3/lib/python3.7/site-packages (from Flask->flask_heroku) (1.1.0)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in ./anaconda3/lib/python3.7/site-packages (from Jinja2>=2.10.1->Flask->flask_heroku) (1.1.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install flask_sqlalchemy\n",
    "!pip install flask_heroku"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, url_for\n",
    "from flask_sqlalchemy import SQLAlchemy\n",
    "import sys\n",
    "import json\n",
    "from sqlalchemy import create_engine\n",
    "from flask_heroku import Heroku\n",
    "app = Flask(__name__)\n",
    "app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False\n",
    "heroku = Heroku(app)\n",
    "db = SQLAlchemy(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sqlalchemy import Column, Integer, String, Float"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "ename": "ArgumentError",
     "evalue": "Mapper mapped class Location->brewerylocations could not assemble any primary key columns for mapped table 'brewerylocations'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mArgumentError\u001b[0m                             Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-46-3dc7abe4384e>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     18\u001b[0m     \u001b[0mupdateDate\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdb\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mColumn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mString\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 20\u001b[0;31m \u001b[0;32mclass\u001b[0m \u001b[0mLocation\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdb\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mModel\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     21\u001b[0m      \u001b[0m__tablename__\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'brewerylocations'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0mid\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdb\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mColumn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mInteger\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/flask_sqlalchemy/model.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(cls, name, bases, d)\u001b[0m\n\u001b[1;32m     65\u001b[0m             \u001b[0mcls\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__tablename__\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcamel_to_snake_case\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcls\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__name__\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     66\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 67\u001b[0;31m         \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mNameMetaMixin\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcls\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbases\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0md\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     68\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     69\u001b[0m         \u001b[0;31m# __table_cls__ has run at this point\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/flask_sqlalchemy/model.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(cls, name, bases, d)\u001b[0m\n\u001b[1;32m    119\u001b[0m         )\n\u001b[1;32m    120\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 121\u001b[0;31m         \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mBindMetaMixin\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcls\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbases\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0md\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    122\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    123\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mbind_key\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcls\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'__table__'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/sqlalchemy/ext/declarative/api.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(cls, classname, bases, dict_)\u001b[0m\n\u001b[1;32m     73\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcls\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mclassname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbases\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdict_\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     74\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;34m\"_decl_class_registry\"\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mcls\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__dict__\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 75\u001b[0;31m             \u001b[0m_as_declarative\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcls\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mclassname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcls\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__dict__\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     76\u001b[0m         \u001b[0mtype\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcls\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mclassname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbases\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdict_\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     77\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/sqlalchemy/ext/declarative/base.py\u001b[0m in \u001b[0;36m_as_declarative\u001b[0;34m(cls, classname, dict_)\u001b[0m\n\u001b[1;32m    129\u001b[0m         \u001b[0;32mreturn\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    130\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 131\u001b[0;31m     \u001b[0m_MapperConfig\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msetup_mapping\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcls\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mclassname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdict_\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    132\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    133\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/sqlalchemy/ext/declarative/base.py\u001b[0m in \u001b[0;36msetup_mapping\u001b[0;34m(cls, cls_, classname, dict_)\u001b[0m\n\u001b[1;32m    158\u001b[0m             \u001b[0mcfg_cls\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_MapperConfig\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    159\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 160\u001b[0;31m         \u001b[0mcfg_cls\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcls_\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mclassname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdict_\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    161\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    162\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcls_\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mclassname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdict_\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/sqlalchemy/ext/declarative/base.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, cls_, classname, dict_)\u001b[0m\n\u001b[1;32m    192\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_setup_inheritance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    193\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 194\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_early_mapping\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    195\u001b[0m         \u001b[0;32mfinally\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    196\u001b[0m             \u001b[0mmapperlib\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_CONFIGURE_MUTEX\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrelease\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/sqlalchemy/ext/declarative/base.py\u001b[0m in \u001b[0;36m_early_mapping\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    197\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    198\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_early_mapping\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 199\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmap\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    200\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    201\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_setup_declared_events\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/sqlalchemy/ext/declarative/base.py\u001b[0m in \u001b[0;36mmap\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    694\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    695\u001b[0m         self.cls.__mapper__ = mp_ = mapper_cls(\n\u001b[0;32m--> 696\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcls\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlocal_table\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmapper_args\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    697\u001b[0m         )\n\u001b[1;32m    698\u001b[0m         \u001b[0;32mdel\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcls\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_sa_declared_attr_reg\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<string>\u001b[0m in \u001b[0;36mmapper\u001b[0;34m(class_, local_table, properties, primary_key, non_primary, inherits, inherit_condition, inherit_foreign_keys, extension, order_by, always_refresh, version_id_col, version_id_generator, polymorphic_on, _polymorphic_map, polymorphic_identity, concrete, with_polymorphic, polymorphic_load, allow_partial_pks, batch, column_prefix, include_properties, exclude_properties, passive_updates, passive_deletes, confirm_deleted_rows, eager_defaults, legacy_is_orphan, _compiled_cache_size)\u001b[0m\n",
      "\u001b[0;32m<string>\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, class_, local_table, properties, primary_key, non_primary, inherits, inherit_condition, inherit_foreign_keys, extension, order_by, always_refresh, version_id_col, version_id_generator, polymorphic_on, _polymorphic_map, polymorphic_identity, concrete, with_polymorphic, polymorphic_load, allow_partial_pks, batch, column_prefix, include_properties, exclude_properties, passive_updates, passive_deletes, confirm_deleted_rows, eager_defaults, legacy_is_orphan, _compiled_cache_size)\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/sqlalchemy/util/deprecations.py\u001b[0m in \u001b[0;36mwarned\u001b[0;34m(fn, *args, **kwargs)\u001b[0m\n\u001b[1;32m    128\u001b[0m                     )\n\u001b[1;32m    129\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 130\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mfn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    131\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    132\u001b[0m         \u001b[0mdoc\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__doc__\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mfn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__doc__\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0;34m\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/sqlalchemy/orm/mapper.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, class_, local_table, properties, primary_key, non_primary, inherits, inherit_condition, inherit_foreign_keys, extension, order_by, always_refresh, version_id_col, version_id_generator, polymorphic_on, _polymorphic_map, polymorphic_identity, concrete, with_polymorphic, polymorphic_load, allow_partial_pks, batch, column_prefix, include_properties, exclude_properties, passive_updates, passive_deletes, confirm_deleted_rows, eager_defaults, legacy_is_orphan, _compiled_cache_size)\u001b[0m\n\u001b[1;32m    714\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_configure_properties\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    715\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_configure_polymorphic_setter\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 716\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_configure_pks\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    717\u001b[0m             \u001b[0mMapper\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_new_mappers\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    718\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_log\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"constructed\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/sqlalchemy/orm/mapper.py\u001b[0m in \u001b[0;36m_configure_pks\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m   1395\u001b[0m                 \u001b[0;34m\"Mapper %s could not assemble any primary \"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1396\u001b[0m                 \u001b[0;34m\"key columns for mapped table '%s'\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1397\u001b[0;31m                 \u001b[0;34m%\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpersist_selectable\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdescription\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1398\u001b[0m             )\n\u001b[1;32m   1399\u001b[0m         elif self.local_table not in self._pks_by_table and isinstance(\n",
      "\u001b[0;31mArgumentError\u001b[0m: Mapper mapped class Location->brewerylocations could not assemble any primary key columns for mapped table 'brewerylocations'"
     ]
    }
   ],
   "source": [
    "class BeerData(db.Model):\n",
    "    __tablename__ = 'beerstyle'\n",
    "    id = db.Column(Integer, primary_key=True)\n",
    "    name = db.Column(String)\n",
    "    shortName = db.Column(String)\n",
    "    description = db.Column(String)\n",
    "    ibuMin = db.Column(Integer)\n",
    "    ibuMax = db.Column(Float)\n",
    "    abvMin = db.Column(Float)\n",
    "    abvMax = db.Column(Float)\n",
    "    srmMin = db.Column(Float)\n",
    "    srmMax = db.Column(Float)\n",
    "    ogMin= db.Column(Float)\n",
    "    ogMax = db.Column(Float)\n",
    "    fgMin = db.Column(Float)\n",
    "    fgMax= db.Column(Float)\n",
    "    createDate = db.Column(String)\n",
    "    updateDate = db.Column(String)\n",
    "    \n",
    "class Location(db.Model):\n",
    "     __tablename__ = 'brewerylocations'\n",
    "id = db.Column(Integer)\n",
    "name = db.Column(String)\n",
    "brewery_type = db.Column(String)\n",
    "street = db.Column(String)\n",
    "city = db.Column(String)\n",
    "state = db.Column(String)\n",
    "postal_code = db.Column(String)\n",
    "country = db.Column(String)\n",
    "longitude = db.Column(Float)\n",
    "latitude = db.Column(Float)\n",
    "phone = db.Column(BIGINT)\n",
    "website_url = db.Column(String)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = create_engine(\"sqlite:///beerSQL.sqlite\")\n",
    "conn = engine.connect()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "Base.metadata.create_all(conn)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sqlalchemy.orm import Session\n",
    "session = Session(bind=engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'BeerData' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-38-d301004f44b9>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mbeer_list\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msession\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquery\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mBeerData\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mbeer_list\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'BeerData' is not defined"
     ]
    }
   ],
   "source": [
    "beer_list = session.query(BeerData)\n",
    "print(beer_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
