import xlsxwriter as xlx

def write_excel(xi,xii):
    workbook = xlx.Workbook('output.xlsx')
    g_xi = workbook.add_worksheet('G11')
    g_xii = workbook.add_worksheet('G12')
    m_headers = workbook.add_format({
    'bold': 1,
    'border': 2,
    'align': 'center',
    'valign': 'vcenter',
    })
    m_days = workbook.add_format({
    'top': 2,
    'right': 2,
    'bold': 1,
    'align': 'center',
    'valign': 'vcenter',
    })
    m_day = workbook.add_format({
    'bottom': 2,
    'bold': 1,
    'align': 'center',
    'valign': 'vcenter',
    })
    m_dayr = workbook.add_format({
    'bottom': 2,
    'right': 2,
    'bold': 1,
    'align': 'center',
    'valign': 'vcenter',
    })
    m_period = workbook.add_format({
    'left': 2,
    'right': 2,
    'bold': 1,
    'align': 'center',
    'valign': 'vcenter',
    })
    m_periodb = workbook.add_format({
    'left': 2,
    'right': 2,
    'bottom': 2,
    'bold': 0,
    'align': 'center',
    'valign': 'vcenter',
    })
    norm = workbook.add_format({
    'bold': 0,
    'align': 'center',
    'valign': 'vcenter',
    })
    normr = workbook.add_format({
    'right': 2,
    'bold': 0,
    'align': 'center',
    'valign': 'vcenter',
    })
    normse = workbook.add_format({
    'right': 2,
    'bottom': 2,
    'bold': 0,
    'align': 'center',
    'valign': 'vcenter',
    })
    norms = workbook.add_format({
    'bottom': 2,
    'bold': 0,
    'align': 'center',
    'valign': 'vcenter',
    })
    def create_sheet(wb, arr):
        wb.merge_range('A1:I2', 'BLOCK A', m_headers)
        wb.merge_range('A3:A4', 'PERIOD', m_headers)
        wb.merge_range('B3:I3', 'DAYS', m_days)
        wb.merge_range('B4:C4', 'MONDAY', m_day)
        wb.merge_range('D4:E4', 'TUESDAY', m_day)
        wb.merge_range('F4:G4', 'WEDNESDAY', m_day)
        wb.merge_range('H4:I4', 'THURSDAY', m_dayr)
        periods = [1,2,"-",3,4,"-",5,6,"-",7]
        for y in range(5,15):
            wb.write(y-1, 0, periods[y-5], m_period)
        wb.write(14, 0, 8, m_periodb)
        wb.merge_range('B5:C5', 'FLAG CEREMONY', norm)
        wb.merge_range('D5:E5', arr[0][0][1], norm)
        wb.merge_range('F5:G5', arr[0][0][2], norm)
        wb.merge_range('H5:I5', arr[0][0][3], normr)
        wb.merge_range('B6:C6', arr[0][1][0], norm)
        wb.merge_range('D6:E6', arr[0][1][1], norm)
        wb.merge_range('F6:G6', arr[0][1][2], norm)
        wb.merge_range('H6:I6', arr[0][1][3], normr)
        wb.merge_range('B7:I7', 'MORNING BREAK', normr)
        wb.merge_range('B8:C8', arr[0][2][0], norm)
        wb.merge_range('D8:E8', arr[0][2][1], norm)
        wb.merge_range('F8:G8', arr[0][2][2], norm)
        wb.merge_range('H8:I8', arr[0][2][3], normr)
        wb.merge_range('B9:C9', arr[0][3][0], norm)
        wb.merge_range('D9:E9', arr[0][3][1], norm)
        wb.merge_range('F9:G9', arr[0][3][2], norm)
        wb.merge_range('H9:I9', arr[0][3][3], normr)
        wb.merge_range('B10:I10', 'LUNCH', normr)
        wb.merge_range('B11:C11', arr[0][4][0], norm)
        wb.merge_range('D11:E11', arr[0][4][1], norm)
        wb.merge_range('F11:G11', arr[0][4][2], norm)
        wb.merge_range('H11:I11', arr[0][4][3], normr)
        wb.merge_range('B12:C12', arr[0][5][0], norm)
        wb.merge_range('D12:E12', arr[0][5][1], norm)
        wb.merge_range('F12:G12', arr[0][5][2], norm)
        wb.merge_range('H12:I12', arr[0][5][3], normr)
        wb.merge_range('B13:I13', 'AFTERNOON BREAK', normr)
        wb.merge_range('B14:C14', arr[0][6][0], norm)
        wb.merge_range('D14:E14', arr[0][6][1], norm)
        wb.merge_range('F14:G14', arr[0][6][2], norm)
        wb.merge_range('H14:I14', arr[0][6][3], normr)
        wb.merge_range('B15:C15', arr[0][7][0], norms)
        wb.merge_range('D15:E15', arr[0][7][1], norms)
        wb.merge_range('F15:G15', arr[0][7][2], norms)
        wb.merge_range('H15:I15', arr[0][7][3], normse)

        wb.merge_range('A17:I18', 'BLOCK B', m_headers)
        wb.merge_range('A19:A20', 'PERIOD', m_headers)
        wb.merge_range('B19:I19', 'DAYS', m_days)
        wb.merge_range('B20:C20', 'MONDAY', m_day)
        wb.merge_range('D20:E20', 'TUESDAY', m_day)
        wb.merge_range('F20:G20', 'WEDNESDAY', m_day)
        wb.merge_range('H20:I20', 'THURSDAY', m_dayr)
        periods = [1,2,"-",3,4,"-",5,6,"-",7]
        for y in range(21,31):
            wb.write(y-1, 0, periods[y-21], m_period)
        wb.write(30, 0, 8, m_periodb)
        wb.merge_range('B21:C21', 'FLAG CEREMONY', norm)
        wb.merge_range('D21:E21', arr[1][0][1], norm)
        wb.merge_range('F21:G21', arr[1][0][2], norm)
        wb.merge_range('H21:I21', arr[1][0][3], normr)
        wb.merge_range('B22:C22', arr[1][1][0], norm)
        wb.merge_range('D22:E22', arr[1][1][1], norm)
        wb.merge_range('F22:G22', arr[1][1][2], norm)
        wb.merge_range('H22:I22', arr[1][1][3], normr)
        wb.merge_range('B23:I23', 'MORNING BREAK', normr)
        wb.merge_range('B24:C24', arr[1][2][0], norm)
        wb.merge_range('D24:E24', arr[1][2][1], norm)
        wb.merge_range('F24:G24', arr[1][2][2], norm)
        wb.merge_range('H24:I24', arr[1][2][3], normr)
        wb.merge_range('B25:C25', arr[1][3][0], norm)
        wb.merge_range('D25:E25', arr[1][3][1], norm)
        wb.merge_range('F25:G25', arr[1][3][2], norm)
        wb.merge_range('H25:I25', arr[1][3][3], normr)
        wb.merge_range('B26:I26', 'LUNCH', normr)
        wb.merge_range('B27:C27', arr[1][4][0], norm)
        wb.merge_range('D27:E27', arr[1][4][1], norm)
        wb.merge_range('F27:G27', arr[1][4][2], norm)
        wb.merge_range('H27:I27', arr[1][4][3], normr)
        wb.merge_range('B28:C28', arr[1][5][0], norm)
        wb.merge_range('D28:E28', arr[1][5][1], norm)
        wb.merge_range('F28:G28', arr[1][5][2], norm)
        wb.merge_range('H28:I28', arr[1][5][3], normr)
        wb.merge_range('B29:I29', 'AFTERNOON BREAK', normr)
        wb.merge_range('B30:C30', arr[1][6][0], norm)
        wb.merge_range('D30:E30', arr[1][6][1], norm)
        wb.merge_range('F30:G30', arr[1][6][2], norm)
        wb.merge_range('H30:I30', arr[1][6][3], normr)
        wb.merge_range('B31:C31', arr[1][7][0], norms)
        wb.merge_range('D31:E31', arr[1][7][1], norms)
        wb.merge_range('F31:G31', arr[1][7][2], norms)
        wb.merge_range('H31:I31', arr[1][7][3], normse)

        wb.merge_range('A33:I34', 'BLOCK C', m_headers)
        wb.merge_range('A35:A36', 'PERIOD', m_headers)
        wb.merge_range('B35:I35', 'DAYS', m_days)
        wb.merge_range('B36:C36', 'MONDAY', m_day)
        wb.merge_range('D36:E36', 'TUESDAY', m_day)
        wb.merge_range('F36:G36', 'WEDNESDAY', m_day)
        wb.merge_range('H36:I36', 'THURSDAY', m_dayr)
        periods = [1,2,"-",3,4,"-",5,6,"-",7]
        for y in range(37,47):
            wb.write(y-1, 0, periods[y-37], m_period)
        wb.write(46, 0, 8, m_periodb)
        wb.merge_range('B37:C37', 'FLAG CEREMONY', norm)
        wb.merge_range('D37:E37', arr[2][0][1], norm)
        wb.merge_range('F37:G37', arr[2][0][2], norm)
        wb.merge_range('H37:I37', arr[2][0][3], normr)
        wb.merge_range('B38:C38', arr[2][1][0], norm)
        wb.merge_range('D38:E38', arr[2][1][1], norm)
        wb.merge_range('F38:G38', arr[2][1][2], norm)
        wb.merge_range('H38:I38', arr[2][1][3], normr)
        wb.merge_range('B39:I39', 'MORNING BREAK', normr)
        wb.merge_range('B40:C40', arr[2][2][0], norm)
        wb.merge_range('D40:E40', arr[2][2][1], norm)
        wb.merge_range('F40:G40', arr[2][2][2], norm)
        wb.merge_range('H40:I40', arr[2][2][3], normr)
        wb.merge_range('B41:C41', arr[2][3][0], norm)
        wb.merge_range('D41:E41', arr[2][3][1], norm)
        wb.merge_range('F41:G41', arr[2][3][2], norm)
        wb.merge_range('H41:I41', arr[2][3][3], normr)
        wb.merge_range('B42:I42', 'LUNCH', normr)
        wb.merge_range('B43:C43', arr[2][4][0], norm)
        wb.merge_range('D43:E43', arr[2][4][1], norm)
        wb.merge_range('F43:G43', arr[2][4][2], norm)
        wb.merge_range('H43:I43', arr[2][4][3], normr)
        wb.merge_range('B44:C44', arr[2][5][0], norm)
        wb.merge_range('D44:E44', arr[2][5][1], norm)
        wb.merge_range('F44:G44', arr[2][5][2], norm)
        wb.merge_range('H44:I44', arr[2][5][3], normr)
        wb.merge_range('B45:I45', 'AFTERNOON BREAK', normr)
        wb.merge_range('B46:C46', arr[2][6][0], norm)
        wb.merge_range('D46:E46', arr[2][6][1], norm)
        wb.merge_range('F46:G46', arr[2][6][2], norm)
        wb.merge_range('H46:I46', arr[2][6][3], normr)
        wb.merge_range('B47:C47', arr[2][7][0], norms)
        wb.merge_range('D47:E47', arr[2][7][1], norms)
        wb.merge_range('F47:G47', arr[2][7][2], norms)
        wb.merge_range('H47:I47', arr[2][7][3], normse)   
    create_sheet(g_xi, xi)
    create_sheet(g_xii, xii)

    workbook.close()