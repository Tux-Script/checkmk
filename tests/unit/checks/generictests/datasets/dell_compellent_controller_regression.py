# -*- encoding: utf-8 -*-

# yapf: disable
# type: ignore


checkname = 'dell_compellent_controller'

info = [
    [u'1', u'1', u'Foo', u'1.2.3.4', u'Model'],
    [u'2', u'999', u'Bar', u'5.6.7.8', u'Model'],
    [u'10', u'2', u'Baz', u'1.3.5.7', u'Model'],
]

discovery = {'': [(u'1', None), (u'2', None), (u'10', None)]}

checks = {
    '': [
        (u'1', {}, [
            (0, 'Status: UP', []),
            (0, u'Model: Model, Name: Foo, Address: 1.2.3.4', []),
        ]),
        (u'2', {}, [
            (3, u'Status: unknown[999]', []),
            (0, u'Model: Model, Name: Bar, Address: 5.6.7.8', []),
        ]),
        (u'10', {}, [
            (2, u'Status: DOWN', []),
            (0, u'Model: Model, Name: Baz, Address: 1.3.5.7', []),
        ]),
    ]
}
