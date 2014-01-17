def check_search_methods(model_instance):
    """
    Call the standard methods used by the search template.  An exception will
    be thrown if the method is not defined
    """
    model_instance.get_absolute_url()
    model_instance.get_summary_description()
