class ContextDataMixin:
    title = None
    active_page = None
    additional_object_list = None

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if self.title is not None:
            context_data['title'] = self.title
        if self.active_page is not None:
            context_data['active_page'] = self.active_page
        if self.additional_object_list is not None:
            context_data['additional_object_list'] = self.additional_object_list
        return context_data
