{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOI7CPVjwuCyll3dESY8rkS",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/waghvaishnav/Deep-Learning-PlayGround-Hub/blob/main/Pytorch(Tensor)%20Basics.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "EpmuhXiOiHt0"
      },
      "outputs": [],
      "source": [
        "import torch"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 0d tensor\n",
        "torch.tensor(5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2rzRd2W2hC5E",
        "outputId": "551e6fe6-6728-4f2a-fe29-860c17e8fbe7"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor(5)"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1d Tensor\n",
        "torch.tensor([12,45,56,321,89])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u_CSebtehphQ",
        "outputId": "3377fc50-64c6-42f6-bdf1-9b3490aeb1ee"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([ 12,  45,  56, 321,  89])"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 2d tensor\n",
        "unit = torch,torch.tensor([[12,32,45],\n",
        "                           [46,32,75],\n",
        "                           [65,89,78]])\n",
        "unit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Elq13SOYifwi",
        "outputId": "637817f1-30b9-44a6-c447-fea9bcebfe3f"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>,\n",
              " tensor([[12, 32, 45],\n",
              "         [46, 32, 75],\n",
              "         [65, 89, 78]]))"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# sales data across different quarter\n",
        "# rows are diffferent products , columns represent different regions\n",
        "\n",
        "q1 = torch.tensor([[200,220,250],     #iphone\n",
        "                   [150,180,210],     # ipad\n",
        "                   [300,330,360]])    #macbook\n",
        "\n",
        "q2 = torch.tensor([[209,231,259],\n",
        "                   [155,192,222],\n",
        "                   [310,340,375]])"
      ],
      "metadata": {
        "id": "ekNzEhyBirnc"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# total sales\n",
        "q1 + q2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YLNUXRSalI7Q",
        "outputId": "f234d2ec-6461-4ca1-8cb5-e3e6b794bccd"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[409, 451, 509],\n",
              "        [305, 372, 432],\n",
              "        [610, 670, 735]])"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# growth in q2 compared to q1\n",
        "q2 - q1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZSKRWwuOlMX0",
        "outputId": "26201319-7ec2-429e-da97-f611eb538ab7"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[ 9, 11,  9],\n",
              "        [ 5, 12, 12],\n",
              "        [10, 10, 15]])"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# growth in q2 compared to q1 in percentage\n",
        "(q2 - q1) * 100 / q1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q6kDja4olYyC",
        "outputId": "f75ba467-a1c5-4d99-8884-c99e7eace682"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[4.5000, 5.0000, 3.6000],\n",
              "        [3.3333, 6.6667, 5.7143],\n",
              "        [3.3333, 3.0303, 4.1667]])"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# units returned\n",
        "return_rate = 0.1\n",
        "return_rate * q1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Hxl1CsnYmUFq",
        "outputId": "c93604cd-f2fd-4c08-9d35-bfb4cafc4a15"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[20., 22., 25.],\n",
              "        [15., 18., 21.],\n",
              "        [30., 33., 36.]])"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# calculates the total profit\n",
        "profit_per_unit = torch.tensor([[12,23,12],\n",
        "                                [65,45,12],\n",
        "                                [65,78,29]])\n",
        "\n",
        "profit_per_unit * q1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iPv0BVUomm8T",
        "outputId": "5398a839-8ea7-4e9c-aa62-4309523d4720"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[ 2400,  5060,  3000],\n",
              "        [ 9750,  8100,  2520],\n",
              "        [19500, 25740, 10440]])"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# product prices\n",
        "product_prices = torch.tensor([[1200,23000,45000]])\n",
        "product_prices"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "25SG02rxnfVx",
        "outputId": "1929ccda-857a-40cd-ac15-c3bfedb701eb"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[ 1200, 23000, 45000]])"
            ]
          },
          "metadata": {},
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "product_prices.t()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CPqeGU5Wo5X6",
        "outputId": "51423bac-5f9a-4f2b-fb64-e1147c63fa9f"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[ 1200],\n",
              "        [23000],\n",
              "        [45000]])"
            ]
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = q1 * product_prices.t()\n",
        "a"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MVCekklio-G_",
        "outputId": "b61a8c21-1420-42db-f5ee-a97b24cd71b2"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[  240000,   264000,   300000],\n",
              "        [ 3450000,  4140000,  4830000],\n",
              "        [13500000, 14850000, 16200000]])"
            ]
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a.sum(dim=0)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "14Lw6UxfruPH",
        "outputId": "5ce60a3b-d574-46be-8ae1-24c480741b47"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([17190000, 19254000, 21330000])"
            ]
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a.sum(dim=1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KfG5e5BJqhFM",
        "outputId": "5b937b04-3bc8-4449-820d-9e9a47b806b2"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([  804000, 12420000, 44550000])"
            ]
          },
          "metadata": {},
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# portfolio composition rows :person , columns : stock,bonds,real_estate\n",
        "\n",
        "portfolio_composition = torch.tensor([[100.0,50.0,30.0],\n",
        "                   [80.0,70.0,20.0],\n",
        "                   [60.0,40.0,90.0]])\n",
        "\n",
        "# price change matrix rows :assets[stocks,bonds,real estate]\n",
        "# columns : economic scenarios [growth, neutral, recession]\n",
        "\n",
        "price_changes = torch.tensor([[1.15,1.05,0.85],\n",
        "                             [1.05,1.02,1.10],\n",
        "                             [1.10,1.00,0.90]])\n",
        "\n",
        "values  = torch.matmul(portfolio_composition,price_changes)\n",
        "values"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0oW36aZJrsbw",
        "outputId": "75344119-d1eb-45fc-a4c3-f123014bb70b"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[200.5000, 186.0000, 167.0000],\n",
              "        [187.5000, 175.4000, 163.0000],\n",
              "        [210.0000, 193.8000, 176.0000]])"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "torch.cuda.is_available()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Gqh3asNl5yFL",
        "outputId": "7e0fa59c-0e6a-48b5-c7be-fb5728f71598"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {},
          "execution_count": 35
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "torch.device"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5mkOHDFv55Uv",
        "outputId": "3bfcf5a7-bca6-41d2-9d68-ea9b2f340188"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "torch.device"
            ]
          },
          "metadata": {},
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data = torch.rand(10000,5,device=\"cpu\")\n",
        "data"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6t06soo365g9",
        "outputId": "84ababd4-2974-4a22-df06-ee6da30bda7a"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[0.3341, 0.3438, 0.7394, 0.2430, 0.3264],\n",
              "        [0.4849, 0.8161, 0.6301, 0.1670, 0.0754],\n",
              "        [0.6240, 0.7569, 0.6207, 0.8912, 0.8023],\n",
              "        ...,\n",
              "        [0.7824, 0.0688, 0.7633, 0.8167, 0.9012],\n",
              "        [0.1180, 0.0118, 0.0616, 0.7633, 0.4138],\n",
              "        [0.9639, 0.9527, 0.5435, 0.2302, 0.0545]])"
            ]
          },
          "metadata": {},
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data.device"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YJTUqyee59iI",
        "outputId": "ae2915ca-be7b-45da-ab43-a8f595e758b4"
      },
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "device(type='cpu')"
            ]
          },
          "metadata": {},
          "execution_count": 43
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# error due to we can try to run on google colab\n",
        "data.to(\"cuda\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 263
        },
        "id": "DzBFp4AD63cH",
        "outputId": "39b7a8e6-ae27-4b80-86d4-46bd4e01466b"
      },
      "execution_count": 49,
      "outputs": [
        {
          "output_type": "error",
          "ename": "AssertionError",
          "evalue": "Torch not compiled with CUDA enabled",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mAssertionError\u001b[0m                            Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-1260865035.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mdata\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mto\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"cuda\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py\u001b[0m in \u001b[0;36m_lazy_init\u001b[0;34m()\u001b[0m\n\u001b[1;32m    415\u001b[0m             )\n\u001b[1;32m    416\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mhasattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtorch\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_C\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"_cuda_getDeviceCount\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 417\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mAssertionError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Torch not compiled with CUDA enabled\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    418\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0m_cudart\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    419\u001b[0m             raise AssertionError(\n",
            "\u001b[0;31mAssertionError\u001b[0m: Torch not compiled with CUDA enabled"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "if torch.cuda.is_available():\n",
        "  device = torch.device(\"cuda\")\n",
        "else:\n",
        "  device = torch.device(\"cpu\")\n",
        "\n",
        "device"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vZyvvX1L7P_0",
        "outputId": "5871bfe5-0509-4139-af5b-683df112c136"
      },
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "device(type='cpu')"
            ]
          },
          "metadata": {},
          "execution_count": 50
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data1 = torch.rand(1000000,5,device=device)\n",
        "data1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zxShxbYW7_dF",
        "outputId": "ac904480-5872-4196-e9ea-f1647814ccf1"
      },
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[0.8722, 0.7632, 0.3085, 0.4539, 0.0229],\n",
              "        [0.4391, 0.6811, 0.5163, 0.9096, 0.5336],\n",
              "        [0.2834, 0.0122, 0.5331, 0.4209, 0.3012],\n",
              "        ...,\n",
              "        [0.3471, 0.8890, 0.1847, 0.3078, 0.6141],\n",
              "        [0.8415, 0.1603, 0.2701, 0.8020, 0.9996],\n",
              "        [0.5781, 0.8929, 0.1382, 0.7288, 0.7418]])"
            ]
          },
          "metadata": {},
          "execution_count": 51
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data1.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HeHseITh8M-E",
        "outputId": "d0b4725c-c846-4d10-df06-66eda88cd785"
      },
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "torch.Size([1000000, 5])"
            ]
          },
          "metadata": {},
          "execution_count": 52
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data[:,2][5]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8Puf_G108Onm",
        "outputId": "c4aab6d8-b3f7-46fa-cf1a-f43857d5191e"
      },
      "execution_count": 54,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor(0.6627)"
            ]
          },
          "metadata": {},
          "execution_count": 54
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data1[:3].shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X14X1U-x8RKQ",
        "outputId": "ead79f58-ce82-45aa-f5b1-64581dabaff3"
      },
      "execution_count": 56,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "torch.Size([3, 5])"
            ]
          },
          "metadata": {},
          "execution_count": 56
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "high_spending_customers = data1[data1[:,1] > 0.5]\n",
        "high_spending_customers.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "C6iTmiOW8pUh",
        "outputId": "96e41b9b-acca-4822-c018-da70a412da9d"
      },
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "torch.Size([500904, 5])"
            ]
          },
          "metadata": {},
          "execution_count": 59
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data1.dtype"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R47P6xc98_PM",
        "outputId": "41d63db8-4472-46d6-e97f-6381f32aecde"
      },
      "execution_count": 60,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "torch.float32"
            ]
          },
          "metadata": {},
          "execution_count": 60
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data1.device"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EZtLa4cg9jRd",
        "outputId": "1587592e-d528-4b6d-e7bd-391d775e763d"
      },
      "execution_count": 61,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "device(type='cpu')"
            ]
          },
          "metadata": {},
          "execution_count": 61
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data1.view(-1)  # flatten to all / multidim into single dim"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8kjNa8kh9n7R",
        "outputId": "45175062-6b3b-4703-e5ae-3086c3f4fe3e"
      },
      "execution_count": 62,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([0.8722, 0.7632, 0.3085,  ..., 0.1382, 0.7288, 0.7418])"
            ]
          },
          "metadata": {},
          "execution_count": 62
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "q1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RGjC4KTp9y_e",
        "outputId": "9078146b-13c9-4576-dff6-4e9177e507d5"
      },
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[200, 220, 250],\n",
              "        [150, 180, 210],\n",
              "        [300, 330, 360]])"
            ]
          },
          "metadata": {},
          "execution_count": 63
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "q1[1,1]  # access the value in row 1,column 1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c9vCVMTq99X4",
        "outputId": "98362861-81ad-4359-8a0f-cd402a459994"
      },
      "execution_count": 65,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor(180)"
            ]
          },
          "metadata": {},
          "execution_count": 65
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# changes the values\n",
        "\n",
        "q1[1,1] = 120\n",
        "q1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6aXEoZF5-EfJ",
        "outputId": "3a3ea086-5523-4df1-c959-ce1784848069"
      },
      "execution_count": 67,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[200, 220, 250],\n",
              "        [150, 120, 210],\n",
              "        [300, 330, 360]])"
            ]
          },
          "metadata": {},
          "execution_count": 67
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "q1.view(9,1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TMJ0cvew-UXW",
        "outputId": "e29720e0-b184-458e-d5d5-f48d2960a96c"
      },
      "execution_count": 71,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[200],\n",
              "        [220],\n",
              "        [250],\n",
              "        [150],\n",
              "        [120],\n",
              "        [210],\n",
              "        [300],\n",
              "        [330],\n",
              "        [360]])"
            ]
          },
          "metadata": {},
          "execution_count": 71
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# returns the tensor of the ones\n",
        "\n",
        "torch.ones(10,5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J8tKZqMs-0mK",
        "outputId": "7c97c4d1-3094-4627-8ef6-a766f5584b12"
      },
      "execution_count": 73,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[1., 1., 1., 1., 1.],\n",
              "        [1., 1., 1., 1., 1.],\n",
              "        [1., 1., 1., 1., 1.],\n",
              "        [1., 1., 1., 1., 1.],\n",
              "        [1., 1., 1., 1., 1.],\n",
              "        [1., 1., 1., 1., 1.],\n",
              "        [1., 1., 1., 1., 1.],\n",
              "        [1., 1., 1., 1., 1.],\n",
              "        [1., 1., 1., 1., 1.],\n",
              "        [1., 1., 1., 1., 1.]])"
            ]
          },
          "metadata": {},
          "execution_count": 73
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "torch.zeros(10,2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tkirZ4SZ-6wa",
        "outputId": "f4dac209-39b3-47ac-9eaf-abad61d8bda6"
      },
      "execution_count": 74,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[0., 0.],\n",
              "        [0., 0.],\n",
              "        [0., 0.],\n",
              "        [0., 0.],\n",
              "        [0., 0.],\n",
              "        [0., 0.],\n",
              "        [0., 0.],\n",
              "        [0., 0.],\n",
              "        [0., 0.],\n",
              "        [0., 0.]])"
            ]
          },
          "metadata": {},
          "execution_count": 74
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# checks for gpu is available or not\n",
        "\n",
        "torch.cuda.is_available()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Kp56p292-9rY",
        "outputId": "f81faf74-359a-41e9-96bb-7d3dc6f1b475"
      },
      "execution_count": 76,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {},
          "execution_count": 76
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "q1.ndim"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rMK393joSgQt",
        "outputId": "34388c5e-9d34-4f18-bb75-2c24f59c6f77"
      },
      "execution_count": 78,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "metadata": {},
          "execution_count": 78
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# checks for datatype of tensor\n",
        "\n",
        "q1.dtype"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EpXvmfdjUuT8",
        "outputId": "1436bf6f-8a74-4d66-e85b-9d4e1716789a"
      },
      "execution_count": 92,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "torch.int64"
            ]
          },
          "metadata": {},
          "execution_count": 92
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# accessing values in tensor\n",
        "\n",
        "q1[:,1][1]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oop1Ygy3U4b3",
        "outputId": "8ef83aec-729e-4d20-88fb-1505b5fb730b"
      },
      "execution_count": 83,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor(120)"
            ]
          },
          "metadata": {},
          "execution_count": 83
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# change datatype in tensor\n",
        "\n",
        "q1.float()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "89Ow3x-jU6c9",
        "outputId": "b0f92927-050b-4bdc-9993-ae93d126be41"
      },
      "execution_count": 93,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[200., 220., 250.],\n",
              "        [150., 120., 210.],\n",
              "        [300., 330., 360.]])"
            ]
          },
          "metadata": {},
          "execution_count": 93
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# change datatype into integer\n",
        "\n",
        "q1.int()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ITwgam7UVgXq",
        "outputId": "2fc9a47b-8c7d-44d1-b031-6572df944fc8"
      },
      "execution_count": 94,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[200, 220, 250],\n",
              "        [150, 120, 210],\n",
              "        [300, 330, 360]], dtype=torch.int32)"
            ]
          },
          "metadata": {},
          "execution_count": 94
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "U1dSRpimXP4r"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}