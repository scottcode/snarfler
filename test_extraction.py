import unittest

import snarfler

test_url = 'https://www.mcmaster.com/#91292a260/=15nn4my'

partname = '18-8 Stainless Steel Socket Head Screw'
part_subtitle = 'M1.6 x 0.35 mm Thread, 3 mm Long'
price = '$11.76'

part_table = (
    ('Thread Size', 'M1.6'),
    ('Thread Pitch', '0.35 mm'),
    ('Length', '3 mm'),
    ('Threading', 'Fully Threaded'),
    ('Head Diameter', '3 mm'),
    ('Head Height', '1.6 mm'),
    ('Drive Size', '1.5 mm'),
    ('Material', '18-8 Stainless Steel'),
    ('Hardness', 'Not Rated'),
    ('Tensile Strength', '70,000 psi'),
    ('Thread Type', 'Metric'),
    ('Thread Spacing', 'Coarse'),
    ('Thread Fit', 'Class 6g'),
    ('Thread Direction', 'Right Hand'),
    ('Head Type', 'Socket'),
    ('Socket Head Profile', 'Standard'),
    ('Drive Style', 'Hex'),
    ('Specifications Met', 'DIN 912'),
    ('System of Measurement', 'Metric'),
    ('RoHS', 'Compliant'),
)

make_error_msg = "{name}: expected '{exp}', got {got}\n".format


class TestRender(unittest.TestCase):
    def tearDown(self):
        snarfler.stop_browser()

    def test_render_has_name(self):
        rendered_html = snarfler.rendered_html_from_url(test_url)
        self.assertIn(
            'Stainless', rendered_html,
            'Part name not found in rendered HTML'
        )
        # self.assertIn(
        #     part_subtitle, str(rendered_html),
        #     'Part subtitle not found in rendered HTML'
        # )

    def test_render_has_price(self):
        rendered_html = snarfler.rendered_html_from_url(test_url)
        self.assertIn(
            price, rendered_html,
            'Price not found in rendered HTML'
        )


class TestExtract(unittest.TestCase):
    def test_partname(self):
        pn = snarfler.partname_from_url(test_url)
        self.assertEqual(
            partname, pn,
            make_error_msg(name='partname', exp=partname, got=pn)
        )

    def test_part_table(self):
        extracted_table = snarfler.table_from_url(test_url)
        self.assertEqual(
            dict(part_table), dict(extracted_table),
            make_error_msg(name='part_table', exp=part_table, got=extracted_table)
        )

    def test_price(self):
        extracted_price = snarfler.price_from_url(test_url)
        self.assertEqual(
            price, extracted_price,
            make_error_msg(name='price', exp=price, got=extracted_price)
        )

