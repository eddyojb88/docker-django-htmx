htmx.defineExtension('echarts', {
    transformResponse: function (text, xhr, elt) {
        // parse json data
        var data = JSON.parse(text);

        // fetch echart element
        var option = data;
        var chartContainer = document.getElementById(data.id);
        var chart = echarts.getInstanceByDom(chartContainer);

        // clean up options and update chart
        delete data.id;
        delete data.label;
        chart.setOption(option);
        return text
        
    },
   handleSwap : function(swapStyle, target, fragment, settleInfo){
      return false;
   },
 
});