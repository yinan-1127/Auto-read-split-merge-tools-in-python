{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "73a28af4-26cf-4986-9700-6748c910fdc0",
   "metadata": {},
   "source": [
    "# 快乐合并！"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c701597-d2ea-40be-9bf4-14bcf2b1ca09",
   "metadata": {},
   "source": [
    "## 完成这个脚本我们需要以下几个条件\n",
    "\n",
    "1. 请把要合并的东西放在和该代码同一个文件夹里\n",
    "2. 请固定他的文件格式\n",
    "3. 然后就可以快乐运行啦！"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b536cd47-9952-4e2b-bb39-848604022090",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "740b90b7-7519-4e21-beb7-1f9278d7ca0a",
   "metadata": {},
   "outputs": [],
   "source": [
    "files = [ i for i in os.listdir() if i.endswith('csv')]\n",
    "files"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b5e56f1-4d8f-4fd7-af00-8d7a1ab4f6e1",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "data = pd.DataFrame()\n",
    "for f in files:\n",
    "    df = pd.read_csv(f)\n",
    "    print(f\"LOADING...... \\n {f} \")\n",
    "    df['filename'] =f.split(\".\")[0]\n",
    "    df['index'] = df.index\n",
    "    data = pd.concat([data,df],axis = 0)\n",
    "    print(f\"SUCCESS! The Merge result is...... \\n {data.shape}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "beca1d8e-329c-4878-b211-ca7993d604fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.iloc[0]['filename']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25c36b53-18a5-45a1-855f-99a96cfc7dd3",
   "metadata": {},
   "outputs": [],
   "source": [
    "  ###实践开始!\n",
    "# import numpy as np\n",
    "# data['score'] = np.nan\n",
    "# data['score'] = data['score'].apply(lambda x:np.random.randn())\n",
    "# data['score'] = data['score'].apply(lambda x: ((x+4)/8)*100)\n",
    "\n",
    "# ###查看分布\n",
    "# import matplotlib.pyplot as plt\n",
    "# data['score'].hist()\n",
    "# plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c613a16-2a52-43de-af60-905463a3f4f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#把打好分的data总文件导入进来\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "12f531c1-c1cc-4847-88b7-edb9d12eef33",
   "metadata": {},
   "outputs": [],
   "source": [
    "samples = list(data['filename'].unique())\n",
    "samples"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4553c68b-b4d4-43ec-9d38-37e4ead85527",
   "metadata": {},
   "outputs": [],
   "source": [
    "grouped_df ={}\n",
    "grouped = data.groupby(\"filename\")\n",
    "print(grouped.count())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "85435a90-9555-4c49-ac1b-3d1149cbf90f",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i,(name,group) in enumerate(grouped):\n",
    "    grouped_df[f'df_{i+1}'] =group.reset_index(drop=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a4f5633-3ae5-44f9-a6c0-20e290ef58fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "grouped_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "935d24ef-2e23-4d45-946b-4a92e6e945f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "for key, value in grouped_df.items():\n",
    "    print(key)\n",
    "    filnm = value.iloc[0]['filename']\n",
    "    print(filnm)\n",
    "    key = pd.DataFrame(value)\n",
    "    print(key.shape)\n",
    "    key.to_csv(f\"{filnm}_score.csv\")\n",
    "    print(f\"{filnm}_score has been saved\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0780207-3b5b-477d-b500-fe5a6a103947",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
