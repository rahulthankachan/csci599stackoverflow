import xlsxwriter

workbook = xlsxwriter.Workbook('Output/charts/questioncount_comparision.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

# Add the worksheet data that the charts will refer to.
headings = ['javascript', 'java', 'c#','php','python','html','c++','sql','objective-c','c']
data = [
    [0, 0, 0, 0, 0, 0, 0, 163, 640, 722, 575, 630, 792, 953, 1011, 1054, 1438, 1562, 1752, 1867, 1749, 2040, 2232, 2306, 2621, 2648, 2983, 3030, 3232, 3507, 3900, 4056, 4067, 4169, 4613, 5025, 5515, 5675, 6860, 7036, 7393, 7779, 8189, 9014, 8311, 8135, 8798, 8419, 9714, 10137, 10878, 10867, 11723, 11422, 12540, 12628, 11316, 12584, 12549, 11923, 14047, 13994, 15630, 15641, 15209, 14796, 17052, 17047, 17925, 19982, 18745, 18254, 21392, 21443, 23009, 21759, 20137, 18630, 20416, 19790, 20222, 21311, 20287, 18842, 20678, 20856, 23108, 23036, 24368, 25107, 27337, 12922, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 227, 1162, 1158, 967, 843, 1164, 1224, 1450, 1551, 1843, 2126, 2298, 2211, 2282, 2526, 2784, 2709, 3759, 3621, 4490, 3927, 4221, 4348, 4584, 4785, 4791, 5113, 5684, 5777, 6658, 6998, 8635, 8030, 8723, 8066, 8289, 8846, 8474, 8675, 9778, 9344, 10307, 11182, 12681, 12287, 12437, 11318, 12498, 12453, 11837, 13762, 13888, 12698, 14026, 14132, 16289, 16607, 15599, 14230, 15429, 15252, 16526, 19064, 19066, 17753, 18974, 19643, 22395, 21275, 18344, 16257, 17715, 16830, 18748, 20035, 20084, 18233, 18355, 18684, 22189, 21863, 20544, 19912, 21508, 10176, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 506, 1652, 1990, 1730, 1598, 2382, 2609, 3166, 3334, 3568, 3897, 4418, 4470, 4377, 4744, 4707, 4517, 5158, 5142, 6098, 5835, 6000, 6210, 6770, 7081, 6494, 6830, 7418, 7202, 8109, 8350, 10123, 9412, 10185, 9918, 9775, 10212, 9442, 9353, 10035, 9465, 10605, 10925, 11849, 11349, 11804, 11525, 12598, 12168, 11438, 12952, 12420, 11150, 13050, 12811, 14563, 14188, 13694, 12982, 14414, 14039, 13954, 15389, 14780, 13823, 15589, 15339, 16447, 15571, 14154, 12775, 13971, 13430, 13829, 14142, 13413, 12314, 13095, 13216, 14946, 14556, 14778, 15069, 16259, 7773, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 163, 493, 625, 508, 481, 649, 778, 910, 977, 1195, 1585, 2044, 2207, 2280, 2390, 2715, 2854, 3474, 3192, 3780, 3684, 4026, 4150, 4688, 5240, 4776, 4606, 5229, 5508, 6554, 6855, 8305, 7839, 8256, 8188, 8875, 9141, 8291, 8255, 8895, 8523, 9540, 10170, 11192, 10709, 11236, 10880, 12089, 12270, 11247, 12110, 12149, 11415, 13254, 13030, 14686, 13892, 13511, 13068, 14720, 14668, 14641, 15785, 15283, 14840, 17318, 17043, 18895, 18224, 15279, 13445, 14740, 14305, 15244, 15486, 14986, 13830, 15331, 15162, 16872, 16659, 16127, 16148, 17910, 8900, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 129, 544, 517, 455, 446, 634, 639, 765, 771, 999, 1045, 1171, 1144, 1176, 1429, 1577, 1597, 1959, 1868, 2084, 1828, 2026, 2233, 2638, 2510, 2268, 2692, 2642, 2516, 2936, 3044, 3789, 3382, 3554, 3498, 3711, 3867, 3546, 3662, 3903, 3660, 4242, 4535, 5088, 4965, 5156, 5323, 5804, 5907, 5313, 6205, 6470, 5820, 6660, 6833, 7743, 8028, 7902, 7669, 8679, 7992, 8047, 9585, 9594, 8552, 9942, 9996, 11530, 10916, 9384, 9020, 10053, 9509, 9548, 10472, 10495, 9750, 10493, 11122, 12605, 12333, 12080, 12824, 13750, 6286, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 108, 331, 328, 325, 296, 404, 473, 520, 519, 669, 751, 962, 974, 918, 972, 1097, 1125, 1406, 1279, 1441, 1444, 1496, 1649, 1990, 2038, 1912, 1885, 2152, 2403, 2765, 2669, 3586, 3274, 3476, 3580, 3884, 4019, 3712, 3709, 3951, 3820, 4376, 4699, 4890, 4895, 5271, 5240, 6042, 6030, 5545, 5802, 6013, 5928, 6778, 6609, 7709, 7657, 7371, 7318, 8537, 8732, 9240, 10064, 9473, 9494, 11406, 10982, 11995, 11368, 10388, 9209, 10121, 9708, 9763, 10113, 9832, 8939, 9936, 9977, 11233, 10909, 11303, 11454, 12197, 5983, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 166, 773, 813, 743, 640, 864, 856, 1062, 1030, 1234, 1267, 1474, 1420, 1475, 1704, 1773, 1668, 2002, 2295, 2452, 2516, 2427, 2850, 2716, 2676, 2770, 2980, 3408, 3176, 3549, 3496, 4231, 4227, 3955, 3865, 3901, 4008, 3985, 4401, 4548, 4436, 4640, 5179, 5316, 5398, 5074, 4725, 5387, 5257, 4997, 6004, 6377, 5784, 6151, 6220, 7353, 7281, 6944, 6284, 6646, 6322, 6638, 8110, 8252, 7128, 7812, 7798, 8819, 8264, 6921, 5841, 6401, 6165, 6691, 7325, 7145, 6578, 6627, 6961, 8021, 7687, 7370, 7110, 7440, 3487, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 148, 500, 539, 413, 426, 589, 668, 663, 741, 849, 929, 1085, 1031, 1361, 1480, 1219, 1187, 1261, 1294, 1468, 1327, 1454, 1636, 1844, 1931, 1750, 1866, 1984, 1899, 2362, 2136, 2675, 2309, 2722, 2666, 2692, 2692, 2607, 2610, 2860, 2614, 2808, 3168, 3640, 3377, 3530, 3339, 3753, 3722, 3647, 4145, 4379, 3914, 4702, 4626, 5307, 5110, 5024, 4785, 5456, 5413, 5952, 6904, 6622, 6318, 7127, 7024, 7834, 7910, 6870, 6452, 6952, 6482, 6740, 5794, 4510, 4421, 4691, 4645, 5284, 5092, 4894, 4952, 5292, 2422, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 20, 50, 93, 107, 118, 139, 205, 289, 358, 498, 489, 680, 696, 689, 750, 755, 784, 993, 1013, 1123, 1158, 1308, 1443, 1961, 1900, 1670, 1763, 1849, 1864, 2199, 2469, 3092, 3307, 3545, 3391, 3786, 3900, 3332, 3322, 3624, 3366, 3812, 3906, 3882, 3971, 3928, 3864, 4380, 4282, 3437, 4185, 3894, 3775, 4150, 3984, 4494, 4156, 3862, 3397, 3813, 3571, 3977, 4495, 4067, 4043, 4442, 4632, 5063, 4712, 4222, 3794, 4231, 3990, 4266, 4172, 3713, 3387, 3370, 3584, 3746, 3740, 3400, 3511, 3872, 1822, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 89, 335, 305, 262, 190, 326, 334, 436, 466, 484, 509, 546, 535, 581, 783, 981, 861, 996, 1044, 1133, 1188, 1193, 1171, 1300, 1389, 1404, 1466, 1687, 1484, 1489, 1656, 2119, 2062, 1850, 1789, 1684, 1839, 1930, 2160, 2235, 2037, 2256, 2442, 2781, 2712, 2519, 2359, 2423, 2358, 2587, 3211, 3242, 2620, 2959, 3169, 3523, 3617, 3266, 3011, 3082, 3051, 3460, 4321, 4354, 3581, 3806, 4040, 4671, 4106, 3342, 2828, 2898, 2761, 3416, 4013, 3890, 3316, 3373, 3533, 4132, 4165, 3713, 3315, 3035, 1480, 0, 0, 0, 0]
]

worksheet.write_row('A1', headings, bold)
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])
worksheet.write_column('D2', data[3])
worksheet.write_column('E2', data[4])
worksheet.write_column('F2', data[5])
worksheet.write_column('G2', data[6])
worksheet.write_column('H2', data[7])
worksheet.write_column('I2', data[8])
worksheet.write_column('J2', data[9])



# Create a new chart object. In this case an embedded chart.
chart1 = workbook.add_chart({'type': 'line'})

# Configure the first series.
chart1.add_series({
    'name':       '=Sheet1!$A$1',
    'categories': '=Sheet1!$A$2:$A$7',
    'values':     '=Sheet1!$A$2:$A$97',
})

# Configure second series. Note use of alternative syntax to define ranges.
chart1.add_series({
    'name':       '=Sheet1!$B$1',
    'categories': '=Sheet1!$B$2:$A$97',
    'values':     '=Sheet1!$B$2:$B$97',
})


chart1.add_series({
    'name':       '=Sheet1!$C$1',
    'categories': '=Sheet1!$C$2:$C$97',
    'values':     '=Sheet1!$C$2:$C$97',
})


chart1.add_series({
    'name':       '=Sheet1!$D$1',
    'categories': '=Sheet1!$D$2:$D$97',
    'values':     '=Sheet1!$D$2:$D$97',
})

chart1.add_series({
    'name':       '=Sheet1!$E$1',
    'categories': '=Sheet1!$E$2:$E$97',
    'values':     '=Sheet1!$E$2:$E$97',
})

chart1.add_series({
    'name':       '=Sheet1!$F$1',
    'categories': '=Sheet1!$F$2:$F$97',
    'values':     '=Sheet1!$F$2:$F$97',
})

chart1.add_series({
    'name':       '=Sheet1!$G$1',
    'categories': '=Sheet1!$G$2:$G$97',
    'values':     '=Sheet1!$G$2:$G$97',
})

chart1.add_series({
    'name':       '=Sheet1!$H$1',
    'categories': '=Sheet1!$H$2:$H$97',
    'values':     '=Sheet1!$H$2:$H$97',
})

chart1.add_series({
    'name':       '=Sheet1!$I$1',
    'categories': '=Sheet1!$I$2:$I$97',
    'values':     '=Sheet1!$I$2:$I$97',
})

chart1.add_series({
    'name':       '=Sheet1!$J$1',
    'categories': '=Sheet1!$J$2:$J$97',
    'values':     '=Sheet1!$J$2:$J$97',
})

# Add a chart title and some axis labels.
chart1.set_title ({'name': 'Duration Analysis'})
chart1.set_x_axis({'name': 'Duration'})
chart1.set_y_axis({'name': 'QuestionCount'})

# Set an Excel chart style. Colors with white outline and shadow.
chart1.set_style(10)

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})


workbook.close()