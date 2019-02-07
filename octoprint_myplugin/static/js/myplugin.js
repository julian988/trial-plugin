$(function() {
    function mypluginViewModel(parameters) {
        var self = this;

	self.test = function(data) {
	  $.ajax({
	      url: /api/plugin/octoprint_myplugin,
	      type: "POST",
	      dataType: "json",
	      data: JSON.stringify(data),command: "turnOn",ip: data.ip()}),
	  contentType: "application/json"
	  });
    };

    ADDITIONAL_VIEWMODELS.push([
        mypluginViewModel,
        ["settingsViewModel"],
        ["#tab_plugin_myplugin"]
    ]);
});
