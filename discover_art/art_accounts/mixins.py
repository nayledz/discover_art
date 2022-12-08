class DisableAutocompleteMixin:
    def _init_bootstrap(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['autocomplete'] = 'off'