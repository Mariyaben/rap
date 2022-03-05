{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled5.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMEGj5m9ew4k09K644bLbrI",
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
        "<a href=\"https://colab.research.google.com/github/Mariyaben/rap/blob/main/q1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "-Viur24VxUtr"
      },
      "outputs": [],
      "source": [
        "#SUM OF DIGITS OF 4 DIGIT NUMBER\n",
        "#REVERSE OF THE NUMBER\n",
        "#DIFFERENCE BETWEEN PRODUCT OF DIGITS AT EVEN POSITION AND PRODUCT OF DIGITS AT EVEN POSITION\n",
        "\n",
        "num=int(input(\"Enter any four digit number\"))\n",
        "p=num\n",
        "a=num%10\n",
        "num=num/10\n",
        "b=num%10\n",
        "num=num/10\n",
        "c=num%10\n",
        "num=num/10\n",
        "d=num%10\n",
        "num=num/10\n",
        "\n",
        "e=a*c\n",
        "f=b*d\n",
        "print(\"sum of digits: \",a+b+c+d)\n",
        "print(\"Difference between product of digits at odd position and product of digits at even position\", e-f)"
      ]
    }
  ]
}