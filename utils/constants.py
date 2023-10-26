from langchain.embeddings import HuggingFaceBgeEmbeddings
from datetime import datetime
from enum import Enum

class HuggingFaceEmbeddings(Enum):
    model_name = "BAAI/bge-large-en-v1.5"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': True} # setting true to compute cosign similarity
    embeddings_dimensions = 768

    @classmethod
    def get_embeddings_model(cls):
        # returning huggingface embeddings model
        # use: model.embed_query("hi this is harrison")
        return HuggingFaceBgeEmbeddings(
            model_name=cls.model_name.value,
            model_kwargs=cls.model_kwargs.value,
            encode_kwargs=cls.encode_kwargs.value,
        )

class VectorDatabaseConstants(Enum):
    VECTOR_EMBEDDING = HuggingFaceEmbeddings.get_embeddings_model()
    top_k = 1000

class Choices(Enum):
    gender = ['Unisex', 'Men', 'Women', 'Boys', 'Girls']

    category = ['Apparel', 'Accessories', 'Footwear', 'Personal Care', 'Free Items', 'Sporting Goods', 'Home']

    sub_category = ['Topwear', 'Bottomwear', 'Watches', 'Socks', 'Shoes', 'Belts', 'Flip Flops',
                    'Bags', 'Innerwear', 'Sandal', 'Shoe Accessories', 'Fragrance', 'Jewellery',
                    'Lips', 'Saree', 'Eyewear', 'Nails', 'Scarves', 'Dress',
                    'Loungewear and Nightwear', 'Wallets', 'Apparel Set', 'Headwear', 'Mufflers',
                    'Skin Care', 'Makeup', 'Free Gifts', 'Ties', 'Accessories', 'Skin',
                    'Beauty Accessories', 'Water Bottle', 'Eyes', 'Bath and Body', 'Gloves',
                    'Sports Accessories', 'Cufflinks', 'Sports Equipment', 'Stoles', 'Hair',
                    'Perfumes', 'Home Furnishing', 'Umbrellas', 'Wristbands', 'Vouchers']

    article_type = ['Shirts', 'Jeans', 'Watches', 'Track Pants', 'Tshirts', 'Socks', 'Casual Shoes',
                    'Belts', 'Flip Flops', 'Handbags', 'Tops', 'Bra', 'Sandals', 'Shoe Accessories',
                    'Sweatshirts', 'Deodorant', 'Formal Shoes', 'Bracelet', 'Lipstick', 'Flats',
                    'Kurtas', 'Waistcoat', 'Sports Shoes', 'Shorts', 'Briefs', 'Sarees',
                    'Perfume and Body Mist', 'Heels', 'Sunglasses', 'Innerwear Vests', 'Pendant',
                    'Nail Polish', 'Laptop Bag', 'Scarves', 'Rain Jacket', 'Dresses',
                    'Night suits', 'Skirts', 'Wallets', 'Blazers', 'Ring', 'Kurta Sets', 'Clutches',
                    'Shrug', 'Backpacks', 'Caps', 'Trousers', 'Earrings', 'Camisoles', 'Boxers',
                    'Jewellery Set', 'Dupatta', 'Capris', 'Lip Gloss', 'Bath Robe', 'Mufflers',
                    'Tunics', 'Jackets', 'Trunk', 'Lounge Pants', 'Face Wash and Cleanser',
                    'Necklace and Chains', 'Duffel Bag', 'Sports Sandals',
                    'Foundation and Primer', 'Sweaters', 'Free Gifts', 'Trolley Bag',
                    'Tracksuits', 'Swimwear', 'Shoe Laces', 'Fragrance Gift Set', 'Bangle',
                    'Nightdress', 'Ties', 'Baby Dolls', 'Leggings', 'Highlighter and Blush',
                    'Travel Accessory', 'Kurtis', 'Mobile Pouch', 'Messenger Bag', 'Lip Care',
                    'Face Moisturisers', 'Compact', 'Eye Cream', 'Accessory Gift Set',
                    'Beauty Accessory', 'Jumpsuit', 'Kajal and Eyeliner', 'Water Bottle',
                    'Suspenders', 'Lip Liner', 'Robe', 'Salwar and Dupatta', 'Patiala',
                    'Stockings', 'Eyeshadow', 'Headband', 'Tights', 'Nail Essentials', 'Churidar',
                    'Lounge Tshirts', 'Face Scrub and Exfoliator', 'Lounge Shorts', 'Gloves',
                    'Mask and Peel', 'Wristbands', 'Tablet Sleeve', 'Ties and Cufflinks',
                    'Footballs', 'Stoles', 'Shapewear', 'Nehru Jackets', 'Salwar', 'Cufflinks',
                    'Jeggings', 'Hair Colour', 'Concealer', 'Rompers', 'Body Lotion', 'Sunscreen',
                    'Booties', 'Waist Pouch', 'Hair Accessory', 'Rucksacks', 'Basketballs',
                    'Lehenga Choli', 'Clothing Set', 'Mascara', 'Toner', 'Cushion Covers',
                    'Key chain', 'Makeup Remover', 'Lip Plumper', 'Umbrellas',
                    'Face Serum and Gel', 'Hat', 'Mens Grooming Kit', 'Rain Trousers',
                    'Body Wash and Scrub', 'Suits', 'Ipad']



    usage = ['Casual', 'Ethnic', 'Formal', 'Sports', 'Smart Casual', 'Travel', 'Party', 'Home']

    @classmethod
    def get_seasons(self):
        now = datetime.now()
        current_month = now.month

        # Define the date ranges for each season based on months
        seasons = {
            'Spring': (3, 4, 5),
            'Summer': (6, 7, 8),
            'Fall': (9, 10, 11),
            'Winter': (12, 1, 2)
        }

        # Determine the current season
        current_season = None
        for season, months in seasons.items():
            if current_month in months:
                current_season = season
                break

        if current_season is None:
            return None  # Couldn't determine the current season

        # Rearrange the seasons
        season_list = ['Spring', 'Summer', 'Fall', 'Winter']
        current_index = season_list.index(current_season)

        reshuffled_seasons = []
        for i in range(len(season_list)):
            reshuffled_seasons.append(season_list[(current_index + i) % len(season_list)])

        return reshuffled_seasons
