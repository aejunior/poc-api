import scrapy


class AngeloniSpider(scrapy.Spider):
    name = "angeloni_spider"
    start_urls = [
		'https://www.angeloni.com.br/super/busca/?Nrpp=12&Ns=dim.product.inStock%7C1%7C%7Csku.activePrice%7C0&Ntt=Picanha+Bovina',
		]

    def parse(self, response):
        BOX_PRODUCT = '.box-produto.p-relative'
        NAME_PRODUCT = "h2 ::text"
        SELECTOR_TYPE_PRICE = "span.box-produto__preco__tipo ::text"
        SELECTOR_UNI_PRICE = "span.box-produto__preco__valor ::text"
        SELECTOR_CENT_PRICE = "span.box-produto__preco__centavos::text"
        for product in response.css(BOX_PRODUCT):
            if product.css(SELECTOR_TYPE_PRICE).extract_first():
                yield {
                    'produto': product.css(NAME_PRODUCT).extract_first().strip(),
                    'preco': 
                        product.css(SELECTOR_TYPE_PRICE).extract_first()+ " " +
                        product.css(SELECTOR_UNI_PRICE).extract_first()+
                        product.css(SELECTOR_CENT_PRICE).extract_first()
                }
            else:
                pass
