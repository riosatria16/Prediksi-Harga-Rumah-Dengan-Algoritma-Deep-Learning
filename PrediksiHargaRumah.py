{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "eETldQIF39Kq"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "import seaborn as sns\n",
        "from sklearn.linear_model import LinearRegression\n",
        "from sklearn.model_selection import train_test_split"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "wjh3Hgkz53My"
      },
      "outputs": [],
      "source": [
        "df = pd.read_csv('kc_house_data.csv', usecols=['bedrooms', 'bathrooms', 'sqft_living', 'grade', 'price', 'yr_built'])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kB6tVCaMdeSl"
      },
      "source": [
        "#- Melihat 5 baris teratas dari data.\n",
        "#- Independent variabel(x) adalah bedrooms, bathrooms, sqft_living, grade, yr_built.\n",
        "#- Dependent variabel(y) adalah price."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "h45VHk5h68DS",
        "outputId": "e22a3bbd-4f95-414b-ec75-79cf23674070"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-fde2091a-06bb-4061-ba41-d6575cde88d1\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>price</th>\n",
              "      <th>bedrooms</th>\n",
              "      <th>bathrooms</th>\n",
              "      <th>sqft_living</th>\n",
              "      <th>grade</th>\n",
              "      <th>yr_built</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>221900.0</td>\n",
              "      <td>3</td>\n",
              "      <td>1.00</td>\n",
              "      <td>1180</td>\n",
              "      <td>7</td>\n",
              "      <td>1955</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>538000.0</td>\n",
              "      <td>3</td>\n",
              "      <td>2.25</td>\n",
              "      <td>2570</td>\n",
              "      <td>7</td>\n",
              "      <td>1951</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>180000.0</td>\n",
              "      <td>2</td>\n",
              "      <td>1.00</td>\n",
              "      <td>770</td>\n",
              "      <td>6</td>\n",
              "      <td>1933</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>604000.0</td>\n",
              "      <td>4</td>\n",
              "      <td>3.00</td>\n",
              "      <td>1960</td>\n",
              "      <td>7</td>\n",
              "      <td>1965</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>510000.0</td>\n",
              "      <td>3</td>\n",
              "      <td>2.00</td>\n",
              "      <td>1680</td>\n",
              "      <td>8</td>\n",
              "      <td>1987</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-fde2091a-06bb-4061-ba41-d6575cde88d1')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-fde2091a-06bb-4061-ba41-d6575cde88d1 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-fde2091a-06bb-4061-ba41-d6575cde88d1');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "      price  bedrooms  bathrooms  sqft_living  grade  yr_built\n",
              "0  221900.0         3       1.00         1180      7      1955\n",
              "1  538000.0         3       2.25         2570      7      1951\n",
              "2  180000.0         2       1.00          770      6      1933\n",
              "3  604000.0         4       3.00         1960      7      1965\n",
              "4  510000.0         3       2.00         1680      8      1987"
            ]
          },
          "execution_count": 5,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df.head()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7778ESco7YCK"
      },
      "source": [
        "### Penjelasan setiap kolom:\n",
        "### 1. bedrooms = Jumlah kamar tidur\n",
        "### 2. bathrooms = Jumlah kamar mandi\n",
        "### 3. sqft_living = Luas rumah dalam satuan sqft\n",
        "### 4. grade = Grading system dari pemerintah King County US\n",
        "### 5. yr_built = Tahun dimana rumah dibangun\n",
        "### 6. price = Harga dari rumah (US$)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IUiiakkq7dSY",
        "outputId": "79109425-c0d0-4a7f-affd-e985f7d6f7b5"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(21613, 6)"
            ]
          },
          "execution_count": 6,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#Mengetahui jumlah kolom dan baris dari data.\n",
        "#Datanya mempunya 6 kolom (features) dengan 21613 baris.\n",
        "df.shape"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2AWiivYq7uYf",
        "outputId": "86ea4833-5db9-4558-dc44-2be7e5c68bb1"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 21613 entries, 0 to 21612\n",
            "Data columns (total 6 columns):\n",
            " #   Column       Non-Null Count  Dtype  \n",
            "---  ------       --------------  -----  \n",
            " 0   price        21613 non-null  float64\n",
            " 1   bedrooms     21613 non-null  int64  \n",
            " 2   bathrooms    21613 non-null  float64\n",
            " 3   sqft_living  21613 non-null  int64  \n",
            " 4   grade        21613 non-null  int64  \n",
            " 5   yr_built     21613 non-null  int64  \n",
            "dtypes: float64(2), int64(4)\n",
            "memory usage: 1013.2 KB\n"
          ]
        }
      ],
      "source": [
        "#Melihat informasi data mulai dari jumlah data, tipe data, memory yang digunakan dll.\n",
        "#Dapat dilihat bahwa seluruh data sudah di dalam bentuk numerik.\n",
        "df.info()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "QMugVr_L8JCp",
        "outputId": "9986ae3d-f133-4b58-ab26-5ff9ad578ade"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-7857072a-e738-45aa-b29a-402998a9c2c0\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>price</th>\n",
              "      <th>bedrooms</th>\n",
              "      <th>bathrooms</th>\n",
              "      <th>sqft_living</th>\n",
              "      <th>grade</th>\n",
              "      <th>yr_built</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>2.161300e+04</td>\n",
              "      <td>21613.000000</td>\n",
              "      <td>21613.000000</td>\n",
              "      <td>21613.000000</td>\n",
              "      <td>21613.000000</td>\n",
              "      <td>21613.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>5.400881e+05</td>\n",
              "      <td>3.370842</td>\n",
              "      <td>2.114757</td>\n",
              "      <td>2079.899736</td>\n",
              "      <td>7.656873</td>\n",
              "      <td>1971.005136</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>3.671272e+05</td>\n",
              "      <td>0.930062</td>\n",
              "      <td>0.770163</td>\n",
              "      <td>918.440897</td>\n",
              "      <td>1.175459</td>\n",
              "      <td>29.373411</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>7.500000e+04</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>290.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1900.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>3.219500e+05</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.750000</td>\n",
              "      <td>1427.000000</td>\n",
              "      <td>7.000000</td>\n",
              "      <td>1951.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>4.500000e+05</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>2.250000</td>\n",
              "      <td>1910.000000</td>\n",
              "      <td>7.000000</td>\n",
              "      <td>1975.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>6.450000e+05</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>2.500000</td>\n",
              "      <td>2550.000000</td>\n",
              "      <td>8.000000</td>\n",
              "      <td>1997.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>7.700000e+06</td>\n",
              "      <td>33.000000</td>\n",
              "      <td>8.000000</td>\n",
              "      <td>13540.000000</td>\n",
              "      <td>13.000000</td>\n",
              "      <td>2015.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-7857072a-e738-45aa-b29a-402998a9c2c0')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-7857072a-e738-45aa-b29a-402998a9c2c0 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-7857072a-e738-45aa-b29a-402998a9c2c0');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "              price      bedrooms     bathrooms   sqft_living         grade  \\\n",
              "count  2.161300e+04  21613.000000  21613.000000  21613.000000  21613.000000   \n",
              "mean   5.400881e+05      3.370842      2.114757   2079.899736      7.656873   \n",
              "std    3.671272e+05      0.930062      0.770163    918.440897      1.175459   \n",
              "min    7.500000e+04      0.000000      0.000000    290.000000      1.000000   \n",
              "25%    3.219500e+05      3.000000      1.750000   1427.000000      7.000000   \n",
              "50%    4.500000e+05      3.000000      2.250000   1910.000000      7.000000   \n",
              "75%    6.450000e+05      4.000000      2.500000   2550.000000      8.000000   \n",
              "max    7.700000e+06     33.000000      8.000000  13540.000000     13.000000   \n",
              "\n",
              "           yr_built  \n",
              "count  21613.000000  \n",
              "mean    1971.005136  \n",
              "std       29.373411  \n",
              "min     1900.000000  \n",
              "25%     1951.000000  \n",
              "50%     1975.000000  \n",
              "75%     1997.000000  \n",
              "max     2015.000000  "
            ]
          },
          "execution_count": 8,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#Melihat statistical description dari data mulai dari mean, kuartil, standard deviation dll.\n",
        "df.describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "id": "FMVIi9A58SxY"
      },
      "outputs": [],
      "source": [
        "#Merubah tipe data dari bathrooms yang semula float menjadi int.\n",
        "df['bathrooms'] = df['bathrooms'].astype('int')\n",
        "#Mengganti nilai 33 menjadi 3.\n",
        "df['bedrooms'] = df['bedrooms'].replace(33,3)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IlpfKOLw8ufh",
        "outputId": "53085d71-7659-4785-ca5b-a3fbb8b38b23"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "price          0\n",
              "bedrooms       0\n",
              "bathrooms      0\n",
              "sqft_living    0\n",
              "grade          0\n",
              "yr_built       0\n",
              "dtype: int64"
            ]
          },
          "execution_count": 10,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#Mencari dan menangani missing values/data kosong atau tidak.\n",
        "#Ternyata datanya sudah tidak ada missing values.\n",
        "df.isnull().sum()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Jcqp0o0R88EA"
      },
      "source": [
        "### Langkah selanjutnya adalah melakukan Exploratory Data Analysis(EDA) untuk mengenal data lebih jauh"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 334
        },
        "id": "-NsuzKEX9M0x",
        "outputId": "d4bc1c90-2786-4e1b-a623-d4b876af4310"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 864x288 with 2 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "#Univariate analysis bedrooms/Kamar Tidur\n",
        "f = plt.figure(figsize=(12,4))\n",
        "f.add_subplot(1,2,1)\n",
        "sns.countplot(df['bedrooms'])\n",
        "f.add_subplot(1,2,2)\n",
        "plt.boxplot(df['bedrooms'])\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WPJNpzH89a8w"
      },
      "source": [
        "### - Dapat dilihat bahwa sebagian besar jumlah kamar tidur itu di angka 3 dan 4.\n",
        "### - Data memiliki banyak outliers."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 334
        },
        "id": "_Y-TJWcG9sfa",
        "outputId": "58cc068b-c4fc-46c3-a4a9-9dfd370bf097"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 864x288 with 2 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "#Univariate analysis bathrooms/Kamar Mandi\n",
        "\n",
        "f = plt.figure(figsize=(12,4))\n",
        "f.add_subplot(1,2,1)\n",
        "sns.countplot(df['bathrooms'])\n",
        "f.add_subplot(1,2,2)\n",
        "plt.boxplot(df['bathrooms'])\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "88SaYU3p-aUi"
      },
      "source": [
        "### - Jumlah kamar mandi paling banyak berada pada angka 1 dan 2.\n",
        "\n",
        "### - Yang menarik disini adalah dimana ada rumah yang tidak ada kamar mandinya atau jumlahnya 0.\n",
        "\n",
        "### - Nilai outlier sendiri lumayan banyak.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 266
        },
        "id": "_hxLEJQB-1-r",
        "outputId": "91bd529f-e363-4f16-df00-ec9b1f5615f7"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 864x288 with 2 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "#Univariate analysis sqft_living/Luas Rumah\n",
        "\n",
        "f = plt.figure(figsize=(12,4))\n",
        "f.add_subplot(1,2,1)\n",
        "df['sqft_living'].plot(kind='kde')\n",
        "f.add_subplot(1,2,2)\n",
        "plt.boxplot(df['sqft_living'])\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eSaMt-l3_J9N"
      },
      "source": [
        "### - Density dari distribusi luas rumah berada di sekitar angka 2000an.\n",
        "\n",
        "### - Banyak terdapat outliers."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 334
        },
        "id": "nW7oFoby_jLD",
        "outputId": "0b13a9be-9987-421e-f127-188eb6c0d7bc"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 864x288 with 2 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "#Univariate analysis grade./ Kualitas (Sistem Dari US)\n",
        "\n",
        "f = plt.figure(figsize=(12,4))\n",
        "f.add_subplot(1,2,1)\n",
        "sns.countplot(df['grade'])\n",
        "f.add_subplot(1,2,2)\n",
        "plt.boxplot(df['grade'])\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_j7-47fUAlEH"
      },
      "source": [
        "### - Sebagian besar rumah di County King US memiliki grade 7 dan 8.\n",
        "\n",
        "### - Dilihat dari boxplot, data memiliki beberapa outliers."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 554
        },
        "id": "UHGU4j0nBLh7",
        "outputId": "9473db64-90d9-4d91-f985-1442cb83e63f"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 1440x576 with 2 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "#Univariate analysis yr_built/tahun rumah dibangun.\n",
        "\n",
        "f = plt.figure(figsize=(20,8))\n",
        "f.add_subplot(1,2,1)\n",
        "sns.countplot(df['yr_built'])\n",
        "f.add_subplot(1,2,2)\n",
        "plt.boxplot(df['yr_built'])\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "V_hR9WzSBpzr"
      },
      "source": [
        "### - Dapat dilihat bahwa semakin tua umur dari rumah, maka semakin sedikit orang yang menjual rumahnya tersebut.\n",
        "\n",
        "### - Density terdapat di sekitar tahun 1980an.\n",
        "\n",
        "### - Data tidak memiliki outliers."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 403
        },
        "id": "b6ke6chbCRa1",
        "outputId": "a9e09b14-258b-4fea-893e-71d2852c1c50"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/axisgrid.py:2076: UserWarning: The `size` parameter has been renamed to `height`; please update your code.\n",
            "  warnings.warn(msg, UserWarning)\n"
          ]
        },
        {
          "data": {
            "text/plain": [
              "<seaborn.axisgrid.PairGrid at 0x7f20d1b06950>"
            ]
          },
          "execution_count": 16,
          "metadata": {},
          "output_type": "execute_result"
        },
        {
          "data": {
            "text/plain": [
              "<Figure size 720x576 with 0 Axes>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "image/png": "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",
            "text/plain": [
              "<Figure size 1350x360 with 5 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "#Bivariate analysis antara independent variable dan dependent variable.\n",
        "\n",
        "plt.figure(figsize=(10,8))\n",
        "sns.pairplot(data=df, x_vars=['bedrooms', 'bathrooms', 'sqft_living', 'grade', 'yr_built'], y_vars=['price'], size=5, aspect=0.75)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 272
        },
        "id": "AAotv6OGCnwr",
        "outputId": "258cbb90-53b0-4356-9ad9-4d246c3ce97c"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:2: FutureWarning: this method is deprecated in favour of `Styler.format(precision=..)`\n",
            "  \n"
          ]
        },
        {
          "data": {
            "text/html": [
              "<style type=\"text/css\">\n",
              "#T_704f0_row0_col0, #T_704f0_row1_col1, #T_704f0_row2_col2, #T_704f0_row3_col3, #T_704f0_row4_col4, #T_704f0_row5_col5 {\n",
              "  background-color: #023858;\n",
              "  color: #f1f1f1;\n",
              "}\n",
              "#T_704f0_row0_col1 {\n",
              "  background-color: #dfddec;\n",
              "  color: #000000;\n",
              "}\n",
              "#T_704f0_row0_col2 {\n",
              "  background-color: #eae6f1;\n",
              "  color: #000000;\n",
              "}\n",
              "#T_704f0_row0_col3 {\n",
              "  background-color: #549cc7;\n",
              "  color: #f1f1f1;\n",
              "}\n",
              "#T_704f0_row0_col4 {\n",
              "  background-color: #7eadd1;\n",
              "  color: #f1f1f1;\n",
              "}\n",
              "#T_704f0_row0_col5, #T_704f0_row1_col4, #T_704f0_row5_col0, #T_704f0_row5_col1, #T_704f0_row5_col2, #T_704f0_row5_col3 {\n",
              "  background-color: #fff7fb;\n",
              "  color: #000000;\n",
              "}\n",
              "#T_704f0_row1_col0 {\n",
              "  background-color: #c8cde4;\n",
              "  color: #000000;\n",
              "}\n",
              "#T_704f0_row1_col2 {\n",
              "  background-color: #f2ecf5;\n",
              "  color: #000000;\n",
              "}\n",
              "#T_704f0_row1_col3, #T_704f0_row2_col5 {\n",
              "  background-color: #9cb9d9;\n",
              "  color: #000000;\n",
              "}\n",
              "#T_704f0_row1_col5 {\n",
              "  background-color: #eee9f3;\n",
              "  color: #000000;\n",
              "}\n",
              "#T_704f0_row2_col0 {\n",
              "  background-color: #7bacd1;\n",
              "  color: #f1f1f1;\n",
              "}\n",
              "#T_704f0_row2_col1, #T_704f0_row2_col4 {\n",
              "  background-color: #a4bcda;\n",
              "  color: #000000;\n",
              "}\n",
              "#T_704f0_row2_col3 {\n",
              "  background-color: #589ec8;\n",
              "  color: #f1f1f1;\n",
              "}\n",
              "#T_704f0_row3_col0 {\n",
              "  background-color: #1e80b8;\n",
              "  color: #f1f1f1;\n",
              "}\n",
              "#T_704f0_row3_col1 {\n",
              "  background-color: #6da6cd;\n",
              "  color: #f1f1f1;\n",
              "}\n",
              "#T_704f0_row3_col2 {\n",
              "  background-color: #81aed2;\n",
              "  color: #f1f1f1;\n",
              "}\n",
              "#T_704f0_row3_col4 {\n",
              "  background-color: #358fc0;\n",
              "  color: #f1f1f1;\n",
              "}\n",
              "#T_704f0_row3_col5 {\n",
              "  background-color: #c6cce3;\n",
              "  color: #000000;\n",
              "}\n",
              "#T_704f0_row4_col0, #T_704f0_row4_col3 {\n",
              "  background-color: #2c89bd;\n",
              "  color: #f1f1f1;\n",
              "}\n",
              "#T_704f0_row4_col1 {\n",
              "  background-color: #d1d2e6;\n",
              "  color: #000000;\n",
              "}\n",
              "#T_704f0_row4_col2 {\n",
              "  background-color: #bdc8e1;\n",
              "  color: #000000;\n",
              "}\n",
              "#T_704f0_row4_col5 {\n",
              "  background-color: #96b6d7;\n",
              "  color: #000000;\n",
              "}\n",
              "#T_704f0_row5_col4 {\n",
              "  background-color: #ece7f2;\n",
              "  color: #000000;\n",
              "}\n",
              "</style>\n",
              "<table id=\"T_704f0_\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr>\n",
              "      <th class=\"blank level0\" >&nbsp;</th>\n",
              "      <th class=\"col_heading level0 col0\" >price</th>\n",
              "      <th class=\"col_heading level0 col1\" >bedrooms</th>\n",
              "      <th class=\"col_heading level0 col2\" >bathrooms</th>\n",
              "      <th class=\"col_heading level0 col3\" >sqft_living</th>\n",
              "      <th class=\"col_heading level0 col4\" >grade</th>\n",
              "      <th class=\"col_heading level0 col5\" >yr_built</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th id=\"T_704f0_level0_row0\" class=\"row_heading level0 row0\" >price</th>\n",
              "      <td id=\"T_704f0_row0_col0\" class=\"data row0 col0\" >1.00</td>\n",
              "      <td id=\"T_704f0_row0_col1\" class=\"data row0 col1\" >0.32</td>\n",
              "      <td id=\"T_704f0_row0_col2\" class=\"data row0 col2\" >0.51</td>\n",
              "      <td id=\"T_704f0_row0_col3\" class=\"data row0 col3\" >0.70</td>\n",
              "      <td id=\"T_704f0_row0_col4\" class=\"data row0 col4\" >0.67</td>\n",
              "      <td id=\"T_704f0_row0_col5\" class=\"data row0 col5\" >0.05</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th id=\"T_704f0_level0_row1\" class=\"row_heading level0 row1\" >bedrooms</th>\n",
              "      <td id=\"T_704f0_row1_col0\" class=\"data row1 col0\" >0.32</td>\n",
              "      <td id=\"T_704f0_row1_col1\" class=\"data row1 col1\" >1.00</td>\n",
              "      <td id=\"T_704f0_row1_col2\" class=\"data row1 col2\" >0.48</td>\n",
              "      <td id=\"T_704f0_row1_col3\" class=\"data row1 col3\" >0.59</td>\n",
              "      <td id=\"T_704f0_row1_col4\" class=\"data row1 col4\" >0.37</td>\n",
              "      <td id=\"T_704f0_row1_col5\" class=\"data row1 col5\" >0.16</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th id=\"T_704f0_level0_row2\" class=\"row_heading level0 row2\" >bathrooms</th>\n",
              "      <td id=\"T_704f0_row2_col0\" class=\"data row2 col0\" >0.51</td>\n",
              "      <td id=\"T_704f0_row2_col1\" class=\"data row2 col1\" >0.48</td>\n",
              "      <td id=\"T_704f0_row2_col2\" class=\"data row2 col2\" >1.00</td>\n",
              "      <td id=\"T_704f0_row2_col3\" class=\"data row2 col3\" >0.70</td>\n",
              "      <td id=\"T_704f0_row2_col4\" class=\"data row2 col4\" >0.61</td>\n",
              "      <td id=\"T_704f0_row2_col5\" class=\"data row2 col5\" >0.43</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th id=\"T_704f0_level0_row3\" class=\"row_heading level0 row3\" >sqft_living</th>\n",
              "      <td id=\"T_704f0_row3_col0\" class=\"data row3 col0\" >0.70</td>\n",
              "      <td id=\"T_704f0_row3_col1\" class=\"data row3 col1\" >0.59</td>\n",
              "      <td id=\"T_704f0_row3_col2\" class=\"data row3 col2\" >0.70</td>\n",
              "      <td id=\"T_704f0_row3_col3\" class=\"data row3 col3\" >1.00</td>\n",
              "      <td id=\"T_704f0_row3_col4\" class=\"data row3 col4\" >0.76</td>\n",
              "      <td id=\"T_704f0_row3_col5\" class=\"data row3 col5\" >0.32</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th id=\"T_704f0_level0_row4\" class=\"row_heading level0 row4\" >grade</th>\n",
              "      <td id=\"T_704f0_row4_col0\" class=\"data row4 col0\" >0.67</td>\n",
              "      <td id=\"T_704f0_row4_col1\" class=\"data row4 col1\" >0.37</td>\n",
              "      <td id=\"T_704f0_row4_col2\" class=\"data row4 col2\" >0.61</td>\n",
              "      <td id=\"T_704f0_row4_col3\" class=\"data row4 col3\" >0.76</td>\n",
              "      <td id=\"T_704f0_row4_col4\" class=\"data row4 col4\" >1.00</td>\n",
              "      <td id=\"T_704f0_row4_col5\" class=\"data row4 col5\" >0.45</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th id=\"T_704f0_level0_row5\" class=\"row_heading level0 row5\" >yr_built</th>\n",
              "      <td id=\"T_704f0_row5_col0\" class=\"data row5 col0\" >0.05</td>\n",
              "      <td id=\"T_704f0_row5_col1\" class=\"data row5 col1\" >0.16</td>\n",
              "      <td id=\"T_704f0_row5_col2\" class=\"data row5 col2\" >0.43</td>\n",
              "      <td id=\"T_704f0_row5_col3\" class=\"data row5 col3\" >0.32</td>\n",
              "      <td id=\"T_704f0_row5_col4\" class=\"data row5 col4\" >0.45</td>\n",
              "      <td id=\"T_704f0_row5_col5\" class=\"data row5 col5\" >1.00</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n"
            ],
            "text/plain": [
              "<pandas.io.formats.style.Styler at 0x7f20d1920890>"
            ]
          },
          "execution_count": 17,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#Mengetahui nilai korelasi dari independent variable dan dependent variable.\n",
        "df.corr().style.background_gradient().set_precision(2)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vIvg7NQIFZqP"
      },
      "source": [
        "### - Dari tabel korelasi dan gambar pairplot, dapat dilihat bahwa sqft_living mempunyai hubungan linear positif yang sangat kuat dengan price jika dibandingkan yang lain.\n",
        "\n",
        "### - Nilai korelasi yr_built hampir mendekati nol yang menandakan bahwa usia rumah tidak mempengaruhi pada harga rumah."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WnF4QrrOFjo_"
      },
      "source": [
        "# **Setelah saya mengetahui karakteristik dari datanya, mari langsung lanjutkan ke tahapan modelling.**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VF1DJf8VF2wZ",
        "outputId": "61e5b796-7818-40a4-b0f2-d9847c552e8c"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[-53061.75464279  64658.55790617    188.90926343 131290.89536823\n",
            "  -3969.55831454]\n",
            "7031568.245717696\n"
          ]
        }
      ],
      "source": [
        "#Pertama, buat variabel x dan y.\n",
        "x = df.drop(columns='price')\n",
        "y = df['price']\n",
        "#Kedua, saya split data menjadi training and testing dengan porsi 80:20.\n",
        "x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)\n",
        "#Ketiga, saya bikin object linear regresi.\n",
        "lin_reg = LinearRegression()\n",
        "#Keempat, train the model menggunakan training data yang sudah displit.\n",
        "lin_reg.fit(x_train, y_train)\n",
        "#Kelima, cari tau nilai slope/koefisien (m) dan intercept (b).\n",
        "print(lin_reg.coef_)\n",
        "print(lin_reg.intercept_)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jE-op9r-GqSA",
        "outputId": "f7cec682-dfc0-477d-d53e-96823e0da5cc"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "0.61251132869411"
            ]
          },
          "execution_count": 19,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#Keenam, cari tahu accuracy score dari model menggunakan testing data yang sudah displit.\n",
        "lin_reg.score(x_test, y_test)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Og5hk7qXG4fV"
      },
      "source": [
        "### Model Machine Learning saya mendapatkan accuracy score sebesar 61.13%. Cukup baik untuk iterasi pertama."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YAHFLW0NIvQn"
      },
      "source": [
        "# **Langkah terakhir ada melakukan prediksi terhadap kriteria rumah idaman dari Saya.**\n",
        "\n",
        "### saya ingin membeli rumah kriteria sebagai berikut:\n",
        "### 1. Jumlah bedrooms = 2\n",
        "### 2. Jumlah bathrooms = 2\n",
        "### 3. Luas rumahnya = 1900 sqft\n",
        "### 4. Dengan grade 8\n",
        "### 5. Tahun pembuatan rumahnya tahun 1989"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "H8tAwpZRJSSh",
        "outputId": "be0a759a-0667-4cf5-9663-64a1c79de4ec"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/sklearn/base.py:451: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
            "  \"X does not have valid feature names, but\"\n"
          ]
        },
        {
          "data": {
            "text/plain": [
              "array([568565.12809136])"
            ]
          },
          "execution_count": 20,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#Prediksi harga rumah idaman Saya.\n",
        "lin_reg.predict([[2,2,1900,8,1989]])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lgOrsnR7JhvI"
      },
      "source": [
        "# Harga rumah idaman Saya adalah sekitar 568565 US$/ RP 8.633.943.807"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "BDwCnjKbgTgK"
      },
      "source": [
        "### SELESAI : Terima Kasih"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "collapsed_sections": [],
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
