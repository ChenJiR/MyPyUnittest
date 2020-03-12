def handle_excel_params(params):
    params = str(params)
    try:
        result = str('{:g}'.format(float(params)))
    except Exception:
        result = str(params)
    return result
