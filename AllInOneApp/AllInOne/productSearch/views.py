from django.shortcuts import render
import requests

def SearchProduct(request):
    search_result = {}
    products = {}
    if 'search_keyword' in request.GET:
        search_keyword = request.GET['search_keyword']
        url = 'https://price-api.datayuge.com/api/v1/compare/search?api_key=F2LlBTOApk0KLp3ZDOCUmSNQ1zLSIgAHBJD&product='+search_keyword
        response = requests.get(url)
        search_result = response.json()
        products = search_result['data']
    return render(request, 'productSearch/productSearch.html', {'products': products})

def ProductDetail(request,productId):
    search_result = {}
    productDetail = {}
    productStores = {}
    stores = []
    url = 'https://price-api.datayuge.com/api/v1/compare/detail?api_key=F2LlBTOApk0KLp3ZDOCUmSNQ1zLSIgAHBJD&id='+productId
    response = requests.get(url)
    search_result = response.json()
    productDetail = search_result['data']

    for store in productDetail['stores']:
        stores.append(store[list(store)[0]])

    return render(request, 'productSearch/productDetail.html',
     {  'product': productDetail,
        'stores':stores
    })


def ProductSpecs(request,productId):
    search_result = {}
    productDetail = {}
    sub_spec_keys = []
    url = 'https://price-api.datayuge.com/api/v1/compare/specs?api_key=F2LlBTOApk0KLp3ZDOCUmSNQ1zLSIgAHBJD&id='+productId
    response = requests.get(url)
    search_result = response.json()
    productSpecs = search_result['data']
    main_specs = productSpecs['main_specs']
    sub_specs = productSpecs['sub_specs']
    sub_spec_keys = list(sub_specs)
    print(sub_specs)
    return render(request, 'productSearch/productSpecs.html',
     {  'mainSpecs': main_specs,
        'subSpecs':sub_specs,
        'sub_spec_keys':sub_spec_keys
    })
