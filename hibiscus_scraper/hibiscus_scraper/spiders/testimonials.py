import scrapy


class TestimonialsSpider(scrapy.Spider):
    name = "testimonials"
    allowed_domains = ["hibiscus.services"]
    start_urls = ["https://hibiscus.services/"]
        
    def parse(self, response):

        testimonials = response.css('div.swiper-slide')  

        for testimonial in testimonials:
            yield {
                'Image': testimonial.css('img::attr(src)').get(),
                'Name': testimonial.css('h2::text').get(),  
                'Designation': testimonial.css('h3::text').get(), 
                'Introduction' : testimonial.css('p::text').get(),
            }

