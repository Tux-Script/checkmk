# -*- encoding: utf-8 -*-

# yapf: disable
# type: ignore

checkname = 'zfsget'

info = [
    ['bpool', 'name', 'bpool', '-'], ['bpool', 'quota', '0', 'default'],
    ['bpool', 'used', '21947036798826', '-'],
    ['bpool', 'available', '11329512075414', '-'],
    ['bpool', 'mountpoint', '/bpool', 'default'],
    ['bpool', 'type', 'filesystem', '-'],
    ['bpool/acs_fs', 'name', 'bpool/acs_fs', '-'],
    ['bpool/acs_fs', 'quota', '0', 'default'],
    ['bpool/acs_fs', 'used', '4829131610', '-'],
    ['bpool/acs_fs', 'available', '11329512075414', '-'],
    ['bpool/acs_fs', 'mountpoint', '/backup/acs', 'local'],
    ['bpool/acs_fs', 'type', 'filesystem', '-'], ['[df]'],
    ['/', '10255636', '1836517', '8419119', '18%', '/'],
    ['/dev', '10255636', '1836517', '8419119', '18%', '/dev'],
    ['proc', '0', '0', '0', '0%', '/proc'],
    ['ctfs', '0', '0', '0', '0%', '/system/contract'],
    ['mnttab', '0', '0', '0', '0%', '/etc/mnttab'],
    ['objfs', '0', '0', '0', '0%', '/system/object'],
    ['swap', '153480592', '232', '153480360', '1%', '/etc/svc/volatile'],
    [
        '/usr/lib/libc/libc_hwcap1.so.1', '10255636', '1836517', '8419119',
        '18%', '/lib/libc.so.1'
    ], ['fd', '0', '0', '0', '0%', '/dev/fd'],
    ['swap', '2097152', '11064', '2086088', '1%', '/tmp'],
    ['swap', '153480384', '24', '153480360', '1%', '/var/run'],
    ['tsrdb10exp/export', '5128704', '21', '4982717', '1%', '/export'],
    ['tsrdb10exp/export/home', '5128704', '55', '4982717', '1%', '/home'],
    ['tsrdb10exp/export/opt', '5128704', '145743', '4982717', '3%', '/opt'],
    ['tsrdb10exp', '5128704', '21', '4982717', '1%', '/tsrdb10exp'],
    ['tsrdb10dat', '30707712', '19914358', '10789464', '65%', '/u01']
]

discovery = {
    '': [
        ('/', {}), ('/dev/fd', {}), ('/etc/mnttab', {}),
        ('/etc/svc/volatile', {}),
        ('/export', {}), ('/home', {}), ('/opt', {}), ('/proc', {}),
        ('/system/contract', {}), ('/system/object', {}), ('/tmp', {}),
        ('/tsrdb10exp', {}), ('/u01', {}), ('/var/run', {})
    ]
}

checks = {
    '': [
        (
            '/', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [
                (
                    0, '17.91% used (1.75 of 9.78 GB)', [
                        (
                            '/', 1793.4736328125, 8012.215625, 9013.742578125,
                            0, 10015.26953125
                        ), ('fs_size', 10015.26953125, None, None, None, None)
                    ]
                )
            ]
        ),
        (
            '/dev/fd', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [(1, 'Size of filesystem is 0 MB', [])]
        ),
        (
            '/etc/mnttab', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [(1, 'Size of filesystem is 0 MB', [])]
        ),
        (
            '/etc/svc/volatile', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [
                (
                    0, '0.0002% used (232.00 kB of 146.37 GB)', [
                        (
                            '/etc/svc/volatile', 0.2265625, 119906.7125,
                            134895.0515625, 0, 149883.390625
                        ), ('fs_size', 149883.390625, None, None, None, None)
                    ]
                )
            ]
        ),
        (
            '/export', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [
                (
                    0, '0.0004% used (21.00 kB of 4.89 GB)', [
                        ('/export', 0.0205078125, 4006.8, 4507.65, 0, 5008.5),
                        ('fs_size', 5008.5, None, None, None, None)
                    ]
                )
            ]
        ),
        (
            '/home', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [
                (
                    0, '0.001% used (55.00 kB of 4.89 GB)', [
                        ('/home', 0.0537109375, 4006.8, 4507.65, 0, 5008.5),
                        ('fs_size', 5008.5, None, None, None, None)
                    ]
                )
            ]
        ),
        (
            '/opt', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [
                (
                    0, '2.84% used (142.33 MB of 4.89 GB)', [
                        ('/opt', 142.3271484375, 4006.8, 4507.65, 0, 5008.5),
                        ('fs_size', 5008.5, None, None, None, None)
                    ]
                )
            ]
        ),
        (
            '/proc', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [(1, 'Size of filesystem is 0 MB', [])]
        ),
        (
            '/system/contract', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [(1, 'Size of filesystem is 0 MB', [])]
        ),
        (
            '/system/object', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [(1, 'Size of filesystem is 0 MB', [])]
        ),
        (
            '/tmp', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [
                (
                    0, '0.53% used (10.80 MB of 2.00 GB)', [
                        ('/tmp', 10.8046875, 1638.4, 1843.2, 0, 2048.0),
                        ('fs_size', 2048.0, None, None, None, None)
                    ]
                )
            ]
        ),
        (
            '/tsrdb10exp', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [
                (
                    0, '0.0004% used (21.00 kB of 4.89 GB)', [
                        (
                            '/tsrdb10exp', 0.0205078125, 4006.8, 4507.65, 0,
                            5008.5
                        ), ('fs_size', 5008.5, None, None, None, None)
                    ]
                )
            ]
        ),
        (
            '/u01', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [
                (
                    0, '64.85% used (18.99 of 29.29 GB)', [
                        (
                            '/u01', 19447.615234375, 23990.4, 26989.2, 0,
                            29988.0
                        ), ('fs_size', 29988.0, None, None, None, None)
                    ]
                )
            ]
        ),
        (
            '/var/run', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [
                (
                    0, '0.00002% used (24.00 kB of 146.37 GB)', [
                        (
                            '/var/run', 0.0234375, 119906.55, 134894.86875, 0,
                            149883.1875
                        ), ('fs_size', 149883.1875, None, None, None, None)
                    ]
                )
            ]
        )
    ]
}
