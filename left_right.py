import sublime
import sublime_plugin

class next_view_in_group(sublime_plugin.WindowCommand):
	def run(self):
		group = self.window.active_group();
		view = self.window.active_view();
		index = self.window.get_view_index(view)[1];
		num_views = len(self.window.views_in_group(group));

		next_view = view; 
		if(index+1 < num_views):
			next_view = self.window.views_in_group(group)[index+1];
		else:
			next_view = self.window.views_in_group(group)[0]; 

		self.window.focus_view(next_view)

class prev_view_in_group(sublime_plugin.WindowCommand):
	def run(self):
		group = self.window.active_group();
		view = self.window.active_view();
		index = self.window.get_view_index(view)[1];
		num_views = len(self.window.views_in_group(group));

		next_view = view; 
		if(index > 0):
			next_view = self.window.views_in_group(group)[index-1];
		else:
			next_view = self.window.views_in_group(group)[num_views-1]; 

		self.window.focus_view(next_view)
