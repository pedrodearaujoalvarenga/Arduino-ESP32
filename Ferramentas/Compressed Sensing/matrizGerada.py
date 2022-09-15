import matplotlib.pyplot as plt

matriz = [-0.140000000000000,
-0.140000000000000,
-0.140000000000000,
-0.140000000000000,
-0.140000000000000,
-0.140000000000000,
-0.140000000000000,
-0.140000000000000,
-0.140000000000000,
-0.115000000000000,
-0.140000000000000,
-0.140000000000000,
-0.155000000000000,
-0.145000000000000,
-0.130000000000000,
-0.110000000000000,
-0.125000000000000,
-0.125000000000000,
-0.130000000000000,
-0.125000000000000,
-0.100000000000000,
-0.0750000000000000,
-0.0750000000000000,
-0.0700000000000000,
-0.0750000000000000,
-0.0700000000000000,
-0.0600000000000000,
-0.0250000000000000,
-0.0200000000000000,
-0.00500000000000000,
0.00500000000000000,
0.0500000000000000,
0.115000000000000,
0.160000000000000,
0.170000000000000,
0.175000000000000,
0.165000000000000,
0.170000000000000,
0.150000000000000,
0.185000000000000,
0.135000000000000,
0.105000000000000,
0.0800000000000000,
0.0650000000000000,
0.0600000000000000,
0.0600000000000000,
0.0150000000000000,
-0.0250000000000000,
-0.0700000000000000,
-0.0900000000000000,
-0.120000000000000,
-0.130000000000000,
-0.120000000000000,
-0.150000000000000,
-0.170000000000000,
-0.175000000000000,
-0.165000000000000,
-0.145000000000000,
-0.155000000000000,
-0.160000000000000,
-0.160000000000000,
-0.150000000000000,
-0.140000000000000,
-0.120000000000000,
-0.140000000000000,
-0.155000000000000,
-0.155000000000000,
-0.135000000000000,
-0.130000000000000,
-0.110000000000000,
-0.105000000000000,
-0.130000000000000,
-0.140000000000000,
-0.140000000000000,
-0.140000000000000,
-0.100000000000000,
0.0200000000000000,
0.180000000000000,
0.380000000000000,
0.605000000000000,
0.790000000000000,
0.895000000000000,
0.840000000000000,
0.590000000000000,
0.225000000000000,
-0.0550000000000000,
-0.185000000000000,
-0.190000000000000,
-0.195000000000000,
-0.160000000000000,
-0.135000000000000,
-0.125000000000000,
-0.100000000000000,
-0.100000000000000,
-0.120000000000000,
-0.135000000000000,
-0.155000000000000,
-0.150000000000000,
-0.125000000000000,
-0.105000000000000,
-0.100000000000000,
-0.115000000000000,
-0.125000000000000,
-0.120000000000000,
-0.100000000000000,
-0.0950000000000000,
-0.105000000000000,
-0.115000000000000,
-0.120000000000000,
-0.110000000000000,
-0.105000000000000,
-0.0950000000000000,
-0.0950000000000000,
-0.110000000000000,
-0.110000000000000,
-0.105000000000000,
-0.0900000000000000,
-0.0850000000000000,
-0.0900000000000000,
-0.115000000000000,
-0.105000000000000,
-0.0900000000000000,
-0.0850000000000000,
-0.0850000000000000,
-0.0850000000000000,
-0.0900000000000000,
-0.100000000000000,
-0.0950000000000000,
-0.0800000000000000,
-0.0600000000000000,
-0.0750000000000000,
-0.0800000000000000,
-0.0850000000000000,
-0.0750000000000000,
-0.0700000000000000,
-0.0550000000000000,
-0.0700000000000000,
-0.0850000000000000,
-0.0800000000000000,
-0.0850000000000000,
-0.0550000000000000,
-0.0400000000000000,
-0.0500000000000000,
-0.0650000000000000,
-0.0600000000000000,
-0.0650000000000000,
-0.0500000000000000,
-0.0350000000000000,
-0.0450000000000000,
-0.0450000000000000,
-0.0450000000000000,
-0.0450000000000000,
-0.0300000000000000,
-0.0350000000000000,
-0.0200000000000000,
-0.0400000000000000,
-0.0500000000000000,
-0.0550000000000000,
-0.0300000000000000,
-0.0250000000000000,
-0.0300000000000000,
-0.0550000000000000,
-0.0550000000000000,
-0.0500000000000000,
-0.0400000000000000,
-0.0400000000000000,
-0.0500000000000000,
-0.0650000000000000,
-0.0850000000000000,
-0.0800000000000000,
-0.0800000000000000,
-0.0700000000000000,
-0.0700000000000000,
-0.0800000000000000,
-0.0900000000000000,
-0.0900000000000000,
-0.0950000000000000,
-0.0900000000000000,
-0.0900000000000000,
-0.115000000000000,
-0.135000000000000,
-0.115000000000000,
-0.105000000000000,
-0.100000000000000,
-0.110000000000000,
-0.125000000000000,
-0.140000000000000,
-0.140000000000000,
-0.120000000000000,
-0.115000000000000,
-0.130000000000000,
-0.135000000000000,
-0.150000000000000,
-0.145000000000000,
-0.130000000000000,
-0.130000000000000,
-0.145000000000000,
-0.150000000000000,
-0.160000000000000,
-0.150000000000000,
-0.130000000000000,
-0.125000000000000,
-0.125000000000000,
-0.155000000000000,
-0.155000000000000,
-0.155000000000000,
-0.140000000000000,
-0.125000000000000,
-0.130000000000000,
-0.135000000000000,
-0.150000000000000,
-0.155000000000000,
-0.135000000000000,
-0.130000000000000,
-0.135000000000000,
-0.140000000000000,
-0.165000000000000,
-0.150000000000000,
-0.135000000000000,
-0.125000000000000,
-0.145000000000000,
-0.150000000000000,
-0.160000000000000,
-0.155000000000000,
-0.135000000000000,
-0.140000000000000,
-0.150000000000000,
-0.145000000000000,
-0.160000000000000,
-0.155000000000000,
-0.150000000000000,
-0.130000000000000,
-0.125000000000000,
-0.145000000000000,
-0.150000000000000,
-0.145000000000000,
-0.135000000000000,
-0.120000000000000,
-0.130000000000000,
-0.130000000000000,
-0.150000000000000,
-0.130000000000000,
-0.125000000000000,
-0.110000000000000,
-0.120000000000000,
-0.135000000000000,
-0.140000000000000,
-0.130000000000000,
-0.115000000000000,
-0.105000000000000,
-0.110000000000000,
-0.115000000000000,
-0.125000000000000,
-0.125000000000000,
-0.105000000000000,
-0.100000000000000,
-0.105000000000000,
-0.110000000000000,
-0.120000000000000,
-0.110000000000000,
-0.100000000000000,
-0.0800000000000000,
-0.0850000000000000,
-0.120000000000000,
-0.110000000000000,
-0.105000000000000,
-0.105000000000000,
-0.0900000000000000,
-0.0850000000000000,
-0.105000000000000,
-0.120000000000000,
-0.105000000000000,
-0.105000000000000,
-0.0900000000000000,
-0.0900000000000000,
-0.115000000000000,
-0.130000000000000,
-0.110000000000000,
-0.0950000000000000,
-0.0850000000000000,
-0.0950000000000000,
-0.0950000000000000,
-0.120000000000000,
-0.100000000000000,
-0.0900000000000000,
-0.100000000000000,
-0.0950000000000000,
-0.105000000000000,
-0.110000000000000,
-0.100000000000000,
-0.0900000000000000,
-0.0700000000000000,
-0.0850000000000000,
-0.0950000000000000,
-0.110000000000000,
-0.0900000000000000,
-0.0850000000000000,
-0.0750000000000000,
-0.0850000000000000,
-0.0950000000000000,
-0.125000000000000,
-0.0900000000000000,
-0.0700000000000000,
-0.0550000000000000,
-0.0600000000000000,
-0.0450000000000000,
-0.0550000000000000,
-0.0500000000000000,
-0.0200000000000000,
-0.00500000000000000,
0,
0.0200000000000000,
0.0200000000000000,
0.0500000000000000,
0.115000000000000,
0.175000000000000,
0.200000000000000,
0.200000000000000,
0.180000000000000,
0.200000000000000,
0.205000000000000,
0.190000000000000,
0.145000000000000,
0.115000000000000,
0.0950000000000000,
0.0750000000000000,
0.0700000000000000,
0.0650000000000000,
0.0200000000000000,
-0.0200000000000000,
-0.0750000000000000,
-0.0850000000000000,
-0.105000000000000,
-0.100000000000000,
-0.120000000000000,
-0.160000000000000,
-0.160000000000000,
-0.155000000000000,
-0.145000000000000,
-0.130000000000000,
-0.145000000000000,
-0.155000000000000,
-0.150000000000000,
-0.145000000000000,
-0.135000000000000,
-0.115000000000000,
-0.120000000000000,
-0.115000000000000,
-0.125000000000000,
-0.130000000000000,
-0.115000000000000,
-0.105000000000000,
-0.100000000000000,
-0.115000000000000,
-0.155000000000000,
-0.140000000000000,
-0.0400000000000000,
0.140000000000000,
0.365000000000000,
0.570000000000000,
0.735000000000000,
0.805000000000000,
0.725000000000000,
0.465000000000000,
0.150000000000000,
-0.0750000000000000,
-0.175000000000000,
-0.175000000000000,
-0.140000000000000,
-0.110000000000000,
-0.105000000000000,
-0.135000000000000,
-0.155000000000000,
-0.160000000000000,
-0.130000000000000,
-0.120000000000000,
-0.120000000000000,
-0.140000000000000,
-0.150000000000000,
-0.160000000000000,
-0.140000000000000,
-0.120000000000000,
-0.125000000000000,
-0.135000000000000,
-0.160000000000000,
-0.155000000000000,
-0.125000000000000,
-0.110000000000000,
-0.120000000000000,
-0.130000000000000,
-0.120000000000000,
-0.105000000000000,
-0.100000000000000,
-0.0750000000000000,
-0.0750000000000000,
-0.0800000000000000,
-0.0950000000000000,
-0.0850000000000000,
-0.0750000000000000,
-0.0550000000000000,
-0.0550000000000000,
-0.0750000000000000,
-0.0700000000000000,
-0.0750000000000000,
-0.0800000000000000,
-0.0700000000000000,
-0.0850000000000000,
-0.100000000000000,
-0.110000000000000,
-0.100000000000000,
-0.115000000000000,
-0.0850000000000000,
-0.0850000000000000,
-0.105000000000000,
-0.110000000000000,
-0.120000000000000,
-0.120000000000000,
-0.105000000000000,
-0.115000000000000,
-0.120000000000000,
-0.135000000000000,
-0.105000000000000,
-0.100000000000000,
-0.0850000000000000,
-0.0950000000000000,
-0.115000000000000,
-0.115000000000000,
-0.120000000000000,
-0.110000000000000,
-0.0950000000000000,
-0.0950000000000000,
-0.105000000000000,
-0.120000000000000,
-0.110000000000000,
-0.100000000000000,
-0.0850000000000000,
-0.105000000000000,
-0.120000000000000,
-0.125000000000000,
-0.120000000000000,
-0.130000000000000,
-0.115000000000000,
-0.125000000000000,
-0.150000000000000,
-0.175000000000000,
-0.170000000000000,
-0.140000000000000,
-0.145000000000000,
-0.155000000000000,
-0.175000000000000,
-0.185000000000000,
-0.205000000000000,
-0.210000000000000,
-0.190000000000000,
-0.200000000000000,
-0.210000000000000,
-0.220000000000000,
-0.230000000000000,
-0.210000000000000,
-0.190000000000000,
-0.195000000000000,
-0.210000000000000,
-0.240000000000000,
-0.235000000000000,
-0.235000000000000,
-0.210000000000000,
-0.220000000000000,
-0.225000000000000,
-0.245000000000000,
-0.235000000000000,
-0.225000000000000,
-0.220000000000000,
-0.235000000000000,
-0.245000000000000,
-0.260000000000000,
-0.255000000000000,
-0.245000000000000,
-0.230000000000000,
-0.230000000000000,
-0.250000000000000,
-0.270000000000000,
-0.250000000000000,
-0.250000000000000,
-0.260000000000000,
-0.260000000000000,
-0.275000000000000,
-0.290000000000000,
-0.285000000000000,
-0.265000000000000,
-0.260000000000000,
-0.255000000000000,
-0.265000000000000,
-0.275000000000000,
-0.265000000000000,
-0.270000000000000,
-0.265000000000000,
-0.255000000000000,
-0.265000000000000,
-0.280000000000000,
-0.265000000000000,
-0.265000000000000,
-0.250000000000000,
-0.260000000000000,
-0.270000000000000,
-0.270000000000000,
-0.255000000000000,
-0.245000000000000,
-0.225000000000000,
-0.225000000000000,
-0.260000000000000,
-0.265000000000000,
-0.260000000000000,
-0.255000000000000,
-0.245000000000000,
-0.235000000000000,
-0.270000000000000,
-0.250000000000000,
-0.250000000000000,
-0.225000000000000,
-0.225000000000000,
-0.225000000000000,
-0.235000000000000,
-0.245000000000000,
-0.240000000000000,
-0.230000000000000,
-0.225000000000000,
-0.235000000000000,
-0.240000000000000,
-0.250000000000000,
-0.245000000000000,
-0.245000000000000,
-0.190000000000000,
-0.215000000000000,
-0.215000000000000,
-0.235000000000000,
-0.225000000000000,
-0.225000000000000,
-0.220000000000000,
-0.200000000000000,
-0.220000000000000,
-0.230000000000000,
-0.235000000000000,
-0.220000000000000,
-0.205000000000000,
-0.205000000000000,
-0.195000000000000,
-0.230000000000000,
-0.205000000000000,
-0.200000000000000,
-0.190000000000000,
-0.195000000000000,
-0.215000000000000,
-0.215000000000000,
-0.200000000000000,
-0.190000000000000,
-0.170000000000000,
-0.175000000000000,
-0.185000000000000,
-0.210000000000000,
-0.190000000000000,
-0.185000000000000,
-0.185000000000000,
-0.190000000000000,
-0.185000000000000,
-0.200000000000000,
-0.200000000000000,
-0.180000000000000,
-0.180000000000000,
-0.175000000000000,
-0.200000000000000,
-0.195000000000000,
-0.200000000000000,
-0.190000000000000,
-0.190000000000000,
-0.175000000000000,
-0.180000000000000,
-0.200000000000000,
-0.195000000000000,
-0.165000000000000,
-0.155000000000000,
-0.175000000000000,
-0.195000000000000,
-0.195000000000000,
-0.185000000000000,
-0.165000000000000,
-0.150000000000000,
-0.145000000000000,
-0.150000000000000,
-0.170000000000000,
-0.150000000000000,
-0.135000000000000,
-0.105000000000000,
-0.110000000000000,
-0.110000000000000,
-0.100000000000000,
-0.0800000000000000,
-0.0550000000000000,
-0.0150000000000000,
0,
0.0200000000000000,
0.0300000000000000,
0.0550000000000000,
0.0650000000000000,
0.0900000000000000,
0.0900000000000000,
0.0650000000000000,
0.0450000000000000,
0.0500000000000000,
0.0300000000000000,
0.0300000000000000,
-0.0100000000000000,
-0.0250000000000000,
-0.0500000000000000,
-0.0700000000000000,
-0.0900000000000000,
-0.0900000000000000,
-0.145000000000000,
-0.175000000000000,
-0.185000000000000,
-0.205000000000000,
-0.205000000000000,
-0.200000000000000,
-0.200000000000000,
-0.200000000000000,
-0.210000000000000,
-0.215000000000000,
-0.200000000000000,
-0.190000000000000,
-0.190000000000000,
-0.195000000000000,
-0.205000000000000,
-0.185000000000000,
-0.180000000000000,
-0.170000000000000,
-0.165000000000000,
-0.180000000000000,
-0.190000000000000,
-0.195000000000000,
-0.210000000000000,
-0.230000000000000,
-0.215000000000000,
-0.145000000000000,
-0.00500000000000000,
0.190000000000000,
0.415000000000000,
0.615000000000000,
0.695000000000000,
0.580000000000000,
0.275000000000000,
-0.0200000000000000,
-0.195000000000000,
-0.260000000000000,
-0.250000000000000,
-0.245000000000000,
-0.205000000000000,
-0.165000000000000,
-0.155000000000000,
-0.140000000000000,
-0.155000000000000,
-0.180000000000000,
-0.195000000000000,
-0.190000000000000,
-0.185000000000000,
-0.165000000000000,
-0.190000000000000,
-0.180000000000000,
-0.200000000000000,
-0.185000000000000,
-0.175000000000000,
-0.170000000000000,
-0.175000000000000,
-0.175000000000000,
-0.180000000000000,
-0.160000000000000,
-0.160000000000000,
-0.150000000000000,
-0.150000000000000,
-0.155000000000000,
-0.160000000000000,
-0.155000000000000,
-0.145000000000000,
-0.125000000000000,
-0.135000000000000,
-0.150000000000000,
-0.155000000000000,
-0.150000000000000,
-0.135000000000000,
-0.120000000000000,
-0.120000000000000,
-0.130000000000000,
-0.145000000000000,
-0.130000000000000,
-0.125000000000000,
-0.120000000000000,
-0.115000000000000,
-0.125000000000000,
-0.145000000000000,
-0.135000000000000,
-0.130000000000000,
-0.110000000000000,
-0.115000000000000,
-0.110000000000000,
-0.135000000000000,
-0.130000000000000,
-0.105000000000000,
-0.0900000000000000,
-0.100000000000000,
-0.110000000000000,
-0.125000000000000,
-0.100000000000000,
-0.0900000000000000,
-0.0850000000000000,
-0.0950000000000000,
-0.0950000000000000,
-0.0950000000000000,
-0.100000000000000,
-0.0950000000000000,
-0.0850000000000000,
-0.0750000000000000,
-0.100000000000000,
-0.0950000000000000,
-0.0950000000000000,
-0.0850000000000000,
-0.0800000000000000,
-0.0800000000000000,
-0.110000000000000,
-0.135000000000000,
-0.120000000000000,
-0.120000000000000,
-0.105000000000000,
-0.115000000000000,
-0.135000000000000,
-0.145000000000000,
-0.160000000000000,
-0.135000000000000,
-0.140000000000000,
-0.160000000000000,
-0.165000000000000,
-0.185000000000000,
-0.170000000000000,
-0.160000000000000,
-0.150000000000000,
-0.160000000000000,
-0.155000000000000,
-0.175000000000000,
-0.175000000000000,
-0.150000000000000,
-0.145000000000000,
-0.155000000000000,
-0.155000000000000,
-0.180000000000000,
-0.160000000000000,
-0.165000000000000,
-0.150000000000000,
-0.155000000000000,
-0.170000000000000,
-0.185000000000000,
-0.170000000000000,
-0.170000000000000,
-0.160000000000000,
-0.165000000000000,
-0.180000000000000,
-0.190000000000000,
-0.185000000000000,
-0.155000000000000,
-0.155000000000000,
-0.175000000000000,
-0.190000000000000,
-0.190000000000000,
-0.180000000000000,
-0.175000000000000,
-0.160000000000000,
-0.160000000000000,
-0.185000000000000,
-0.185000000000000,
-0.195000000000000,
-0.170000000000000,
-0.170000000000000,
-0.175000000000000,
-0.185000000000000,
-0.185000000000000,
-0.185000000000000,
-0.170000000000000,
-0.155000000000000,
-0.165000000000000,
-0.170000000000000,
-0.190000000000000,
-0.180000000000000,
-0.170000000000000,
-0.160000000000000,
-0.155000000000000,
-0.175000000000000,
-0.180000000000000,
-0.180000000000000,
-0.155000000000000,
-0.160000000000000,
-0.160000000000000,
-0.165000000000000,
-0.165000000000000,
-0.155000000000000,
-0.150000000000000,
-0.125000000000000,
-0.130000000000000,
-0.155000000000000,
-0.170000000000000,
-0.165000000000000,
-0.150000000000000,
-0.130000000000000,
-0.145000000000000,
-0.155000000000000,
-0.170000000000000,
-0.160000000000000,
-0.155000000000000,
-0.145000000000000,
-0.145000000000000,
-0.170000000000000,
-0.165000000000000,
-0.150000000000000,
-0.145000000000000,
-0.140000000000000,
-0.145000000000000,
-0.155000000000000,
-0.175000000000000,
-0.160000000000000,
-0.140000000000000,
-0.115000000000000,
-0.135000000000000,
-0.150000000000000,
-0.150000000000000,
-0.150000000000000,
-0.125000000000000,
-0.115000000000000,
-0.115000000000000,
-0.130000000000000,
-0.150000000000000,
-0.140000000000000,
-0.140000000000000,
-0.120000000000000,
-0.115000000000000,
-0.115000000000000,
-0.110000000000000,
-0.100000000000000,
-0.0700000000000000,
-0.0500000000000000,
-0.0450000000000000,
-0.0400000000000000,
-0.0600000000000000,
-0.0400000000000000,
-0.00500000000000000,
0.0550000000000000,
0.110000000000000,
0.140000000000000,
0.155000000000000,
0.160000000000000,
0.150000000000000,
0.170000000000000,
0.160000000000000,
0.125000000000000,
0.0950000000000000,
0.0800000000000000,
0.0650000000000000,
0.0850000000000000,
0.0650000000000000,
0.0200000000000000,
-0.0250000000000000,
-0.0700000000000000,
-0.0950000000000000,
-0.110000000000000,
-0.130000000000000,
-0.165000000000000,
-0.175000000000000,
-0.185000000000000,
-0.165000000000000,
-0.150000000000000,
-0.155000000000000,
-0.175000000000000,
-0.180000000000000,
-0.160000000000000,
-0.170000000000000,
-0.140000000000000,
-0.130000000000000,
-0.145000000000000,
-0.160000000000000,
-0.160000000000000,
-0.160000000000000,
-0.160000000000000,
-0.145000000000000,
-0.0650000000000000,
0.115000000000000,
0.360000000000000,
0.575000000000000,
0.735000000000000,
0.795000000000000,
0.760000000000000,
0.560000000000000,
0.310000000000000,
0.0500000000000000,
-0.120000000000000,
-0.215000000000000,
-0.245000000000000,
-0.230000000000000,
-0.190000000000000,
-0.150000000000000,
-0.120000000000000,
-0.120000000000000,
-0.155000000000000,
-0.170000000000000,
-0.165000000000000,
-0.150000000000000,
-0.140000000000000,
-0.160000000000000,
-0.160000000000000,
-0.160000000000000,
-0.160000000000000,
-0.150000000000000,
-0.140000000000000,
-0.140000000000000,
-0.155000000000000,
-0.155000000000000,
-0.155000000000000,
-0.140000000000000,
-0.130000000000000,
-0.125000000000000,
-0.125000000000000,
-0.135000000000000,
-0.140000000000000,
-0.120000000000000,
-0.120000000000000,
-0.115000000000000,
-0.120000000000000,
-0.125000000000000,
-0.120000000000000,
-0.100000000000000,
-0.0900000000000000,
-0.0950000000000000,
-0.110000000000000,
-0.105000000000000,
-0.120000000000000,
-0.100000000000000,
-0.0950000000000000,
-0.110000000000000,
-0.105000000000000,
-0.125000000000000,
-0.110000000000000,
-0.105000000000000,
-0.0850000000000000,
-0.0950000000000000,
-0.0950000000000000,
-0.110000000000000,
-0.100000000000000,
-0.0900000000000000,
-0.0700000000000000,
-0.0700000000000000,
-0.0800000000000000,
-0.105000000000000,
-0.0850000000000000,
-0.0750000000000000,
-0.0500000000000000,
-0.0550000000000000,
-0.0600000000000000,
-0.0700000000000000,
-0.0800000000000000,
-0.0750000000000000,
-0.0450000000000000,
-0.0450000000000000,
-0.0600000000000000,
-0.0600000000000000,
-0.0550000000000000,
-0.0450000000000000,
-0.0500000000000000,
-0.0550000000000000,
-0.0550000000000000,
-0.0650000000000000,
-0.0650000000000000,
-0.0400000000000000,
-0.0450000000000000,
-0.0500000000000000,
-0.0700000000000000,
-0.0850000000000000,
-0.0750000000000000,
-0.0650000000000000,
-0.0650000000000000,
-0.0650000000000000,
-0.0800000000000000,
-0.100000000000000,
-0.0950000000000000,
-0.100000000000000,
-0.100000000000000,
-0.105000000000000,
-0.120000000000000,
-0.120000000000000,
-0.130000000000000,
-0.120000000000000,
-0.105000000000000,
-0.120000000000000,
-0.140000000000000,
-0.150000000000000,
-0.130000000000000,
-0.130000000000000,
-0.130000000000000,
-0.135000000000000,
-0.145000000000000,
-0.150000000000000,
-0.140000000000000,
-0.135000000000000,
-0.160000000000000,
-0.165000000000000,
-0.165000000000000,
-0.155000000000000,
-0.150000000000000,
-0.135000000000000,
-0.125000000000000,
-0.160000000000000,
-0.160000000000000,
-0.160000000000000,
-0.150000000000000,
-0.135000000000000,
-0.150000000000000,
-0.150000000000000,
-0.145000000000000,
-0.135000000000000,
-0.120000000000000,
-0.115000000000000,
-0.120000000000000]

plt.plot(matriz)
plt.show()