{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN4Ln2ZHH1b40gwb3di6P6C",
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
        "<a href=\"https://colab.research.google.com/github/rtomek9/DS4003Sprint4/blob/main/Sprint4_DS4003.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-wc848jpmNRS",
        "outputId": "1ed1b991-d14e-457c-bec3-332095f44e95"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting dash\n",
            "  Downloading dash-2.16.1-py3-none-any.whl (10.2 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m10.2/10.2 MB\u001b[0m \u001b[31m18.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: Flask<3.1,>=1.0.4 in /usr/local/lib/python3.10/dist-packages (from dash) (2.2.5)\n",
            "Requirement already satisfied: Werkzeug<3.1 in /usr/local/lib/python3.10/dist-packages (from dash) (3.0.1)\n",
            "Requirement already satisfied: plotly>=5.0.0 in /usr/local/lib/python3.10/dist-packages (from dash) (5.15.0)\n",
            "Collecting dash-html-components==2.0.0 (from dash)\n",
            "  Downloading dash_html_components-2.0.0-py3-none-any.whl (4.1 kB)\n",
            "Collecting dash-core-components==2.0.0 (from dash)\n",
            "  Downloading dash_core_components-2.0.0-py3-none-any.whl (3.8 kB)\n",
            "Collecting dash-table==5.0.0 (from dash)\n",
            "  Downloading dash_table-5.0.0-py3-none-any.whl (3.9 kB)\n",
            "Requirement already satisfied: importlib-metadata in /usr/local/lib/python3.10/dist-packages (from dash) (7.1.0)\n",
            "Requirement already satisfied: typing-extensions>=4.1.1 in /usr/local/lib/python3.10/dist-packages (from dash) (4.10.0)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from dash) (2.31.0)\n",
            "Collecting retrying (from dash)\n",
            "  Downloading retrying-1.3.4-py3-none-any.whl (11 kB)\n",
            "Requirement already satisfied: nest-asyncio in /usr/local/lib/python3.10/dist-packages (from dash) (1.6.0)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.10/dist-packages (from dash) (67.7.2)\n",
            "Requirement already satisfied: Jinja2>=3.0 in /usr/local/lib/python3.10/dist-packages (from Flask<3.1,>=1.0.4->dash) (3.1.3)\n",
            "Requirement already satisfied: itsdangerous>=2.0 in /usr/local/lib/python3.10/dist-packages (from Flask<3.1,>=1.0.4->dash) (2.1.2)\n",
            "Requirement already satisfied: click>=8.0 in /usr/local/lib/python3.10/dist-packages (from Flask<3.1,>=1.0.4->dash) (8.1.7)\n",
            "Requirement already satisfied: tenacity>=6.2.0 in /usr/local/lib/python3.10/dist-packages (from plotly>=5.0.0->dash) (8.2.3)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.10/dist-packages (from plotly>=5.0.0->dash) (24.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.1.1 in /usr/local/lib/python3.10/dist-packages (from Werkzeug<3.1->dash) (2.1.5)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.10/dist-packages (from importlib-metadata->dash) (3.18.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->dash) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->dash) (3.6)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->dash) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->dash) (2024.2.2)\n",
            "Requirement already satisfied: six>=1.7.0 in /usr/local/lib/python3.10/dist-packages (from retrying->dash) (1.16.0)\n",
            "Installing collected packages: dash-table, dash-html-components, dash-core-components, retrying, dash\n",
            "Successfully installed dash-2.16.1 dash-core-components-2.0.0 dash-html-components-2.0.0 dash-table-5.0.0 retrying-1.3.4\n"
          ]
        }
      ],
      "source": [
        "!pip install dash"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import plotly.express as px\n",
        "from dash import Dash, dcc, html, Input, Output, callback\n",
        "from datetime import date\n",
        "import pandas as pd\n",
        "import plotly.graph_objects as go\n",
        "\n",
        "df = pd.read_csv('/content/mydata2.csv')\n",
        "rad_columns = [\"stability\",\t\"rights\",\t\"health\",\t\"safety\",\t\"climate\",\t\"cost\",\t\"popularity\"]\n",
        "range = [0,10,20,30,40,50,60,70,80,90,100]\n",
        "\n",
        "# initialize app\n",
        "external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']\n",
        "app = Dash(__name__, external_stylesheets=external_stylesheets)\n",
        "server = app.server\n",
        "# define layout and elements\n",
        "app.layout = html.Div([\n",
        "    html.H2(\"Oh the Places You'll Go!\"),\n",
        "    html.P(\"The following data come from a variety of reputable sources \"\n",
        "           \"for each different metric: Some are from the World Bank, other metrics \"\n",
        "           \"are compiled from the United Nations, and others are taken from the \"\n",
        "           \"Institute for Economics & Peace. The dataset has then been uploaded \"\n",
        "           \"to Kaggle and is now accessible to all Kaggle users.\"),\n",
        "    html.H4(\"Select the Dates of Arrival & Departure\"),\n",
        "    html.Div([\n",
        "    dcc.DatePickerRange(\n",
        "        id='date-picker-range',\n",
        "        start_date=date(2024, 4, 3),\n",
        "        end_date_placeholder_text='Select a date'\n",
        "    )\n",
        "]),\n",
        "    html.H4(\"Select up to two countries\"),\n",
        "    dcc.Dropdown(\n",
        "                    id='country-dropdown',\n",
        "                   options=[{'label': country, 'value': country} for country in df['country']],\n",
        "                    value=df['country'][:2],  # Pre-select the first two countries\n",
        "                    multi=True  # Set multi attribute to True\n",
        "                ),\n",
        "        html.Div([\n",
        "        dcc.Graph(id='polar-plot', figure={})\n",
        "    ], style={'display': 'inline-block', 'width': '50%'}),\n",
        "    html.Div([\n",
        "        dcc.Graph(id='bar-chart', figure={}),\n",
        "    ], style={'display': 'inline-block', 'width': '50%'}),\n",
        "    html.Div(id='country-info')\n",
        "])\n",
        "\n",
        "@app.callback(\n",
        "   [Output('polar-plot', 'figure'),\n",
        "    Output('bar-chart', 'figure')],\n",
        "   Input('country-dropdown', 'value')\n",
        ")\n",
        "\n",
        "def update_plot(selected_countries):\n",
        "    traces = []\n",
        "    if len(selected_countries) <= 2:\n",
        "        for country in selected_countries:\n",
        "            country_data = df[df['country'] == country]\n",
        "            values = country_data[rad_columns].values.flatten().tolist()\n",
        "            traces.append(go.Scatterpolar(\n",
        "                r=values,\n",
        "                theta=rad_columns,\n",
        "                fill='toself',\n",
        "                name=country\n",
        "            ))\n",
        "        layout = go.Layout(\n",
        "              polar=dict(\n",
        "                 radialaxis=dict(\n",
        "                    visible=True,\n",
        "                    range=[0, 100]\n",
        "                )),\n",
        "            showlegend=True\n",
        "        )\n",
        "        fig = go.Figure(data=traces, layout=layout)\n",
        "    else:\n",
        "        fig = go.Figure()\n",
        "        fig.add_annotation(text=\"Please select up to two countries\", showarrow=False,\n",
        "                           xref='paper', yref='paper', x=0.5, y=0.5, font_size=20)\n",
        "    bar_traces = []\n",
        "    for category in rad_columns:\n",
        "        category_values = df[df['country'].isin(selected_countries)][category]\n",
        "        bar_traces.append(go.Bar(\n",
        "            x=selected_countries,\n",
        "            y=category_values,\n",
        "            name=category\n",
        "        ))\n",
        "    bar_layout = go.Layout(\n",
        "        barmode='stack',\n",
        "        xaxis=dict(title='Country'),\n",
        "        yaxis=dict(title='Value')\n",
        "    )\n",
        "    bar_fig = go.Figure(data=bar_traces, layout=bar_layout)\n",
        "    return fig, bar_fig\n",
        "\n",
        "@app.callback(\n",
        "    Output('country-info', 'children'),\n",
        "    Input('country-dropdown', 'value')\n",
        ")\n",
        "def update_country_info(selected_countries):\n",
        "    info = []\n",
        "    for country in selected_countries:\n",
        "        country_data = df[df['country'] == country]\n",
        "        max_value = country_data[rad_columns].max().idxmax()  # Get column name with max value\n",
        "        min_value = country_data[rad_columns].min().idxmin()  # Get column name with min value\n",
        "        info.append(html.Div([\n",
        "            html.H3(country),\n",
        "            html.P(f\"Strength: {max_value} ({country_data[max_value].max()})\"),\n",
        "            html.P(f\"Weakness: {min_value} ({country_data[min_value].min()})\")\n",
        "        ]))\n",
        "    return info\n",
        "\n",
        "# run app\n",
        "if __name__ == '__main__':\n",
        "    app.run(jupyter_mode='external', debug=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 52
        },
        "id": "ImcI1P0UmPcd",
        "outputId": "d5d92620-202a-4a21-a878-10f18ddd0067"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Dash app running on:\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "(async (port, path, text, element) => {\n",
              "    if (!google.colab.kernel.accessAllowed) {\n",
              "      return;\n",
              "    }\n",
              "    element.appendChild(document.createTextNode(''));\n",
              "    const url = await google.colab.kernel.proxyPort(port);\n",
              "    const anchor = document.createElement('a');\n",
              "    anchor.href = new URL(path, url).toString();\n",
              "    anchor.target = '_blank';\n",
              "    anchor.setAttribute('data-href', url + path);\n",
              "    anchor.textContent = text;\n",
              "    element.appendChild(anchor);\n",
              "  })(8050, \"/\", \"http://127.0.0.1:8050/\", window.element)"
            ]
          },
          "metadata": {}
        }
      ]
    }
  ]
}
