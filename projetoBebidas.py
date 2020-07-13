{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "projetoBebidas.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyM2YYY2/6a9ZEuFa8LTfSUP",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/DihCodigo/datasciencebebidas/blob/master/projetoBebidas.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "smfmKgMEJh6j",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        },
        "outputId": "44549a7b-4994-41b6-fcfa-5d8c25ad6b49"
      },
      "source": [
        "#Este projeto de Data Sciente foi criado por CÉSAR DIEGO e ALESSANDRO\n",
        "#Nossa ideia foi levantar uma pesquisa sobre os países com mais taxa de consumo alcoolico..\n",
        "\n",
        "#para analizar, utilizaremos um link de um arquivo csv para mostrar em graficos.\n",
        "\n",
        "#chamar biblioteca pandas\n",
        "import pandas as pd\n",
        "url = \"https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv\"\n",
        "bebidas = pd.read_csv(url)\n",
        "bebidas.head()\n",
        "\n",
        "#vamos renomear os titulos para ficar mais compreensivo\n",
        "bebidas.columns = [\"País\", \"cerveja_servida\", \"porções_espirituais\", \"porções_vinho\", \"total_alcool\"]\n",
        "bebidas.head()\n",
        "\n",
        "\n",
        "#para simplificar abaixo, mostramos quem bebe mais cerveja, bebidas espirituosas e vinhos\n",
        "\n",
        "#foi colocado um header para mostrar os 5 principais países por porção consumida por pessoa, 2010"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
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
              "      <th>País</th>\n",
              "      <th>cerveja_servida</th>\n",
              "      <th>porções_espirituais</th>\n",
              "      <th>porções_vinho</th>\n",
              "      <th>total_alcool</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Afghanistan</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Albania</td>\n",
              "      <td>89</td>\n",
              "      <td>132</td>\n",
              "      <td>54</td>\n",
              "      <td>4.9</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Algeria</td>\n",
              "      <td>25</td>\n",
              "      <td>0</td>\n",
              "      <td>14</td>\n",
              "      <td>0.7</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Andorra</td>\n",
              "      <td>245</td>\n",
              "      <td>138</td>\n",
              "      <td>312</td>\n",
              "      <td>12.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Angola</td>\n",
              "      <td>217</td>\n",
              "      <td>57</td>\n",
              "      <td>45</td>\n",
              "      <td>5.9</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "          País  cerveja_servida  ...  porções_vinho  total_alcool\n",
              "0  Afghanistan                0  ...              0           0.0\n",
              "1      Albania               89  ...             54           4.9\n",
              "2      Algeria               25  ...             14           0.7\n",
              "3      Andorra              245  ...            312          12.4\n",
              "4       Angola              217  ...             45           5.9\n",
              "\n",
              "[5 rows x 5 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_nHKc1LWLfH8",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 119
        },
        "outputId": "0c3cf82b-4fd3-49a8-b946-9dd357361ebd"
      },
      "source": [
        "#para detalharmos somente o importante que seria o total vamos exibir somente o Id e o total representando cada Id\n",
        "\n",
        "bebidas[\"total_alcool\"].head()\n"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0     0.0\n",
              "1     4.9\n",
              "2     0.7\n",
              "3    12.4\n",
              "4     5.9\n",
              "Name: total_alcool, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FBd5MKUGYLHT",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        },
        "outputId": "98b03b92-9602-4f1f-a1ed-31abf8e5d6c0"
      },
      "source": [
        "bebidas.describe() #ESTATISTICA DESCRITIVA"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
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
              "      <th>cerveja servida</th>\n",
              "      <th>porções espirituais</th>\n",
              "      <th>porções de vinho</th>\n",
              "      <th>total de litros de álcool puro</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>193.000000</td>\n",
              "      <td>193.000000</td>\n",
              "      <td>193.000000</td>\n",
              "      <td>193.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>106.160622</td>\n",
              "      <td>80.994819</td>\n",
              "      <td>49.450777</td>\n",
              "      <td>4.717098</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>101.143103</td>\n",
              "      <td>88.284312</td>\n",
              "      <td>79.697598</td>\n",
              "      <td>3.773298</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>20.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.300000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>76.000000</td>\n",
              "      <td>56.000000</td>\n",
              "      <td>8.000000</td>\n",
              "      <td>4.200000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>188.000000</td>\n",
              "      <td>128.000000</td>\n",
              "      <td>59.000000</td>\n",
              "      <td>7.200000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>376.000000</td>\n",
              "      <td>438.000000</td>\n",
              "      <td>370.000000</td>\n",
              "      <td>14.400000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "       cerveja servida  ...  total de litros de álcool puro\n",
              "count       193.000000  ...                      193.000000\n",
              "mean        106.160622  ...                        4.717098\n",
              "std         101.143103  ...                        3.773298\n",
              "min           0.000000  ...                        0.000000\n",
              "25%          20.000000  ...                        1.300000\n",
              "50%          76.000000  ...                        4.200000\n",
              "75%         188.000000  ...                        7.200000\n",
              "max         376.000000  ...                       14.400000\n",
              "\n",
              "[8 rows x 4 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gQHd6N83YlOQ",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 343
        },
        "outputId": "2afa0142-f786-4dc3-cb27-a1a8251d1bad"
      },
      "source": [
        "!pip install seaborn==0.9.0"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Collecting seaborn==0.9.0\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/a8/76/220ba4420459d9c4c9c9587c6ce607bf56c25b3d3d2de62056efe482dadc/seaborn-0.9.0-py3-none-any.whl (208kB)\n",
            "\u001b[K     |████████████████████████████████| 215kB 2.8MB/s \n",
            "\u001b[?25hRequirement already satisfied: matplotlib>=1.4.3 in /usr/local/lib/python3.6/dist-packages (from seaborn==0.9.0) (3.2.2)\n",
            "Requirement already satisfied: pandas>=0.15.2 in /usr/local/lib/python3.6/dist-packages (from seaborn==0.9.0) (1.0.5)\n",
            "Requirement already satisfied: scipy>=0.14.0 in /usr/local/lib/python3.6/dist-packages (from seaborn==0.9.0) (1.4.1)\n",
            "Requirement already satisfied: numpy>=1.9.3 in /usr/local/lib/python3.6/dist-packages (from seaborn==0.9.0) (1.18.5)\n",
            "Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.6/dist-packages (from matplotlib>=1.4.3->seaborn==0.9.0) (1.2.0)\n",
            "Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.6/dist-packages (from matplotlib>=1.4.3->seaborn==0.9.0) (2.8.1)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.6/dist-packages (from matplotlib>=1.4.3->seaborn==0.9.0) (0.10.0)\n",
            "Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /usr/local/lib/python3.6/dist-packages (from matplotlib>=1.4.3->seaborn==0.9.0) (2.4.7)\n",
            "Requirement already satisfied: pytz>=2017.2 in /usr/local/lib/python3.6/dist-packages (from pandas>=0.15.2->seaborn==0.9.0) (2018.9)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.6/dist-packages (from python-dateutil>=2.1->matplotlib>=1.4.3->seaborn==0.9.0) (1.12.0)\n",
            "Installing collected packages: seaborn\n",
            "  Found existing installation: seaborn 0.10.1\n",
            "    Uninstalling seaborn-0.10.1:\n",
            "      Successfully uninstalled seaborn-0.10.1\n",
            "Successfully installed seaborn-0.9.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "34n91E54YqM4",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 221
        },
        "outputId": "aef7c347-fe8f-4fda-d8c6-9a758f20ca3d"
      },
      "source": [
        "bebidas[\"total_alcool\"].value_counts()"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.0    13\n",
              "0.1     7\n",
              "2.2     6\n",
              "6.3     5\n",
              "6.6     4\n",
              "       ..\n",
              "4.4     1\n",
              "3.1     1\n",
              "9.8     1\n",
              "1.4     1\n",
              "3.9     1\n",
              "Name: total_alcool, Length: 90, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xnRwZAppZDSv",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "outputId": "35806f21-4673-48de-9215-8687aea5090f"
      },
      "source": [
        "bebidas.total_alcool.plot(kind='hist')"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f3a0f54ee48>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 20
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NyoqBUqijQ2r",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 351
        },
        "outputId": "4f8c8396-d3c6-4c48-e946-a0e30ae0027b"
      },
      "source": [
        "import seaborn as sns\n",
        "\n",
        "sns.boxplot(bebidas.total_alcool)"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/statsmodels/tools/_testing.py:19: FutureWarning: pandas.util.testing is deprecated. Use the functions in the public API at pandas.testing instead.\n",
            "  import pandas.util.testing as tm\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f3a04b21c88>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 21
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Jw9fgahHkHqn",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        },
        "outputId": "ebe01871-caa5-4780-aaa1-a90cd789911d"
      },
      "source": [
        "sns.distplot(bebidas.total_alcool)"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f3a046322b0>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 23
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    }
  ]
}