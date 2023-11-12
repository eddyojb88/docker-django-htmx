from django.shortcuts import render
from django.http import HttpResponse
from plotly.offline import plot
import plotly.graph_objs as go
import random

def index(request):
    return render(request, "app/index.html", )


def getlinechart(request):

    if request.htmx:

        fig = go.Figure()

        x=[0,1,2,3,4,5,6,7,8]
        
        # Create a list with 5 random numbers between 0 and 100
        y = [random.randint(1, 100) for _ in range(len(x))]

        scatter = go.Scatter(x=x, y=y,
                            mode='lines+markers', name='test',
                            opacity=0.8, marker_color='hotpink', line=dict(width=4, shape='spline'))
        fig.add_trace(scatter)

        fig.update_layout(showlegend=True,
                        hovermode='closest',
                        margin=dict(l=20, r=20, t=10, b=20),
                        paper_bgcolor="black", plot_bgcolor="black",
                        font_color='white',
                        xaxis={'title': {'text': 'x'}, 'showgrid': False, },
                        yaxis={'title': {'text': '%s' %('y'),}, 'showgrid': False, 
                                },
                        )
        
        plot_div = plot(fig, output_type='div')
        
        context={'plot_div': plot_div}

        return render(request, "app/components/linechart.html", context=context)
    
from .echarts import line_chart, fake_chart_data

CHART_TYPES = {
    "page_views": "Total Page Views",
    "unique_visitors": "Unique Visitors",
    "signups": "Signups"
}


def dashboard_view(request):

    total_page_views = fake_chart_data(7, 'Total Page Views')
    charts = [
        line_chart(total_page_views),
    ]

    context = {"charts": charts}

    return render(request, "app/dashboard.html", context)


def chart_view_hx(request):
    """Returns chart options for echarts"""

    period = request.GET.get("period", "week")
    chart_id = request.GET.get("chart_id")
    chart_type = request.GET.get("chart_type")

    days_in_period = {
        "week": 7,
        "month": 30,
    }
    filter_by = days_in_period.get(period, "week")

    # simulate fetching this from your database
    chart_title = CHART_TYPES.get(chart_type, "page_views")
    chart_data = fake_chart_data(filter_by, chart_title)
    print(chart_data)

    # render the chart and update options to include id
    chart = line_chart(chart_data)
    chart.options["id"] = chart_id
    chart._prepare_render()
    data = chart.json_contents

    response = HttpResponse(content=data)

    return response