# --------------------------------------------------
#  Astrology Horoscope Generator
#     Astrological sign based on month and day of birth
#     information used is from https://en.wikipedia.org/wiki/History_of_astrology
# 
#  Oct 11, 2024  -- @PythonCoderUnicorn
# --------------------------------------------------



from rich.console import Console 
from rich import print
from rich.panel import Panel
from rich.console import group
import random 


console = Console()


class Signs():
  
  def __init__(self) -> None:
    pass

  # ------- astrology unicodes
  aries = "\u2648"
  taurus = "\u2649"
  gemini = "\u264A"
  cancer = "\u264B"
  leo = "\u264C"
  virgo = "\u264D"
  libra = "\u264E"
  scorpio = "\u2650"
  Sagittarius = "\u2651"
  capricorn = "\u2652"
  aquarius = "\u2653"
  pisces = "\u2654"
  # print(scorpio)
  
  # "Capricorn": [(12, 22), (1, 19)] December 22nd to January 19th
  capricorn_dec = list( range(22,32))
  capricorn_jan = list( range(1,20) )
  # "Aquarius": [(1, 20), (2, 18)] # January 20th to February 18th
  aquarius_jan = list( range(20,32))
  aquarius_feb = list( range(1,19))
  # "Pisces": [(2, 19), (3, 20)],    # February 19th to March 20th
  pisces_feb = list( range(19,29))
  pisces_march = list( range(1,21))
  # "Aries": [(3, 21), (4, 19)],      # March 21st to April 19th
  aries_march = list( range(21, 32))
  aries_april = list( range(1, 20))
  # "Taurus": [(4, 20), (5, 20)],     # April 20th to May 20th
  taurus_april = list( range(20,31))
  taurus_may = list( range(1,32))
  # "Gemini": [(5, 21), (6, 20)],      # May 21st to June 20th
  gemini_may = list(range(21,32))
  gemini_june = list(range(1,21))
  # "Cancer": [(6, 21), (7, 22)],     # June 21st to July 22nd
  cancer_june = list(range(21,31))
  cancer_july = list(range(1,23))
  # "Leo": [(7, 23), (8, 22)],       # July 23rd to August 22nd
  leo_july = list(range(23,32))
  leo_aug = list(range(1,23))
  # "Virgo": [(8, 23), (9, 22)],      # August 23rd to September 22nd
  virgo_aug = list( range(23,32))
  virgo_sept = list(range(1,23))
  # "Libra": [(9, 23), (10, 22)],     # September 23rd to October 22nd
  libra_sept = list(range(23,31))
  libra_oct = list(range(1,23))
  # "Scorpio": [(10, 23), (11, 21)],   # October 23rd to November 21st
  scorpio_oct = list(range(23,32))
  scorpio_nov = list(range(1,22))
  # "Sagittarius": [(11, 22), (12, 21)] # November 22nd to December 21st
  Sagittarius_nov = list(range(22,31))
  Sagittarius_dec = list(range(1,22))



  def Sagittarius_data(self):

      zodiac = "Sagittarius"
      readings = [
        f"{zodiac}, your adventurous spirit will be calling this week. Explore new horizons and broaden your perspective. A journey awaits you.",
        f'{zodiac}, this season is the time to shine and try out something new, small steps lead to big changes.',
        f'{zodiac}, this week has been a struggle, but trust in your tenacity and strength to see the positives come to light',
        f'{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.',
        f'{zodiac}, your ambition will drive you forward this week. Set clear goals and work diligently to achieve them. Success is yours for the taking.',
        f"{zodiac}, your intuition will be your guiding light this week. Trust your inner voice and follow your heart. A spiritual journey awaits you.",
        f"{zodiac}, your innovative ideas will be in high demand this week. Share your unique perspective and inspire others. Change is coming.",
        f"{zodiac}, your passion will be ignited this week. Follow your desires and pursue your dreams with intensity. Success is within reach.",
        f"{zodiac}, balance is key this week. Find harmony between your personal and professional life. A new partnership could be on the horizon.",
        f"{zodiac}, focus on self-care and well-being this week. Take time for yourself to recharge and rejuvenate. Your efforts will pay off.",
        f"{zodiac}, your creativity will shine this week. Express yourself freely and let your talents shine. Recognition is on the horizon.",
        f"{zodiac}, your intuition will be sharp this week. Trust your gut and follow your heart. A new adventure awaits you.",
        f"{zodiac}, expect a whirlwind of activity this week. Be prepared to adapt to changing circumstances and embrace new opportunities.",
        f"{zodiac}, focus on nurturing your relationships this week. Spend quality time with loved ones and strengthen your bonds.",
        f"{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.",
      ]
      
      symbol = "Archer"
      element = "Fire"
      quality="Mutable"
      ruler ="Jupiter"
      detriment = "Mercury"
      exalt="South Node"
      fall="North Node"
      
      results = f"""
      [cyan] \u2022 Zodiac symbol: {symbol} \u2022 Zodiac element: {element} \u2022 Zodiac quality: {quality} 
      \u2022 Sign ruler: {ruler} \u2022 Detriment: {detriment} \u2022 Exaltation: {exalt} \u2022 Fall: {fall} [/]
      
      [dark_olive_green2] Backstory [/]:
      [cyan]Greek mythology[/cyan] associates Sagittarius with the centaur Chiron, who mentored Achilles.
      Sagittarius, the [cyan]half human and half horse, is the centaur of mythology[/], the learned healer whose higher intelligence forms a bridge between Earth and Heaven. Also known as the Archer, Sagittarius is represented by the symbol of a bow and arrow.
      As an archer, Sagittarius is said never to fail in hitting the mark and this depiction alludes to the power of prophecy, hence, the claim that seers and prophets are born in this sign
      
      [dark_olive_green2] Horoscope: [/]
      {random.choice(readings)}
      """
      print(Panel(results, title="Astrology Results", subtitle="Enjoy"))
      
      
  def aries_data(self):

      zodiac="Aries"
      readings = [
        f"{zodiac}, your adventurous spirit will be calling this week. Explore new horizons and broaden your perspective. A journey awaits you.",
        f'{zodiac}, this season is the time to shine and try out something new, small steps lead to big changes.',
        f'{zodiac}, this week has been a struggle, but trust in your tenacity and strength to see the positives come to light',
        f'{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.',
        f'{zodiac}, your ambition will drive you forward this week. Set clear goals and work diligently to achieve them. Success is yours for the taking.',
        f"{zodiac}, your intuition will be your guiding light this week. Trust your inner voice and follow your heart. A spiritual journey awaits you.",
        f"{zodiac}, your innovative ideas will be in high demand this week. Share your unique perspective and inspire others. Change is coming.",
        f"{zodiac}, your passion will be ignited this week. Follow your desires and pursue your dreams with intensity. Success is within reach.",
        f"{zodiac}, balance is key this week. Find harmony between your personal and professional life. A new partnership could be on the horizon.",
        f"{zodiac}, focus on self-care and well-being this week. Take time for yourself to recharge and rejuvenate. Your efforts will pay off.",
        f"{zodiac}, your creativity will shine this week. Express yourself freely and let your talents shine. Recognition is on the horizon.",
        f"{zodiac}, your intuition will be sharp this week. Trust your gut and follow your heart. A new adventure awaits you.",
        f"{zodiac}, expect a whirlwind of activity this week. Be prepared to adapt to changing circumstances and embrace new opportunities.",
        f"{zodiac}, focus on nurturing your relationships this week. Spend quality time with loved ones and strengthen your bonds.",
        f"{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.",
      ]
      
      symbol = "Ram"
      element = "Fire"
      quality="Cardinal"
      ruler ="Mars"
      detriment = "Venus"
      exalt="Sun"
      fall="Saturn"
      
      results = f"""
      [cyan] \u2022 Zodiac symbol: {symbol} \u2022 Zodiac element: {element} \u2022 Zodiac quality: {quality} 
      \u2022 Sign ruler: {ruler} \u2022 Detriment: {detriment} \u2022 Exaltation: {exalt} \u2022 Fall: {fall} [/]
      
      [dark_olive_green2] Backstory [/]:
      Aries is one of the six positive signs of the zodiac and it is one of the four modality cardinals of the zodiac. Aries is one of the three fire signs in the zodiac.
      In [cyan]Greek Mythology[/], the symbol of the ram is based on the Chrysomallus, the flying ram that rescued Phrixus and Helle, the children of the Boeotian king Athamas and provided the Golden Fleece. There is no link between Aries and Ares, the god of war.
      
      [dark_olive_green2] Horoscope: [/]
      {random.choice(readings)}
      """
      print(Panel(results, title="Astrology Results", subtitle="Enjoy"))


  def capricorn_data(self):

      zodiac="Capricorn"
      readings = [
        f"{zodiac}, your adventurous spirit will be calling this week. Explore new horizons and broaden your perspective. A journey awaits you.",
        f'{zodiac}, this season is the time to shine and try out something new, small steps lead to big changes.',
        f'{zodiac}, this week has been a struggle, but trust in your tenacity and strength to see the positives come to light',
        f'{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.',
        f'{zodiac}, your ambition will drive you forward this week. Set clear goals and work diligently to achieve them. Success is yours for the taking.',
        f"{zodiac}, your intuition will be your guiding light this week. Trust your inner voice and follow your heart. A spiritual journey awaits you.",
        f"{zodiac}, your innovative ideas will be in high demand this week. Share your unique perspective and inspire others. Change is coming.",
        f"{zodiac}, your passion will be ignited this week. Follow your desires and pursue your dreams with intensity. Success is within reach.",
        f"{zodiac}, balance is key this week. Find harmony between your personal and professional life. A new partnership could be on the horizon.",
        f"{zodiac}, focus on self-care and well-being this week. Take time for yourself to recharge and rejuvenate. Your efforts will pay off.",
        f"{zodiac}, your creativity will shine this week. Express yourself freely and let your talents shine. Recognition is on the horizon.",
        f"{zodiac}, your intuition will be sharp this week. Trust your gut and follow your heart. A new adventure awaits you.",
        f"{zodiac}, expect a whirlwind of activity this week. Be prepared to adapt to changing circumstances and embrace new opportunities.",
        f"{zodiac}, focus on nurturing your relationships this week. Spend quality time with loved ones and strengthen your bonds.",
        f"{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.",
      ]
      
      symbol = "Sea goat"
      element = "Earth"
      quality="Cardinal"
      ruler ="Saturn"
      detriment = "Moon"
      exalt="Mars"
      fall="Jupiter"
      
      
      results = f"""
      [cyan] \u2022 Zodiac symbol: {symbol} \u2022 Zodiac element: {element} \u2022 Zodiac quality: {quality} 
      \u2022 Sign ruler: {ruler} \u2022 Detriment: {detriment} \u2022 Exaltation: {exalt} \u2022 Fall: {fall}[/]
      
      [dark_olive_green2] Backstory [/]:
      Capricorn is one of the three earth signs, alongside Virgo and Taurus. Capricorn is ruled by the planet Saturn and its opposite sign is Cancer.
      In [indian_red ]India[/], the zodiac sign of Capricorn is celebrated as the Makara Sankranti festival, also known in Nepal as Maghe Sankranti
      
      [dark_olive_green2] Horoscope: [/]
      {random.choice(readings)}
      """
      print(Panel(results, title="Astrology Results", subtitle="Enjoy"))


  def aquarius_data(self):

      zodiac="Aquarius"
      readings = [
        f"{zodiac}, your adventurous spirit will be calling this week. Explore new horizons and broaden your perspective. A journey awaits you.",
        f'{zodiac}, this season is the time to shine and try out something new, small steps lead to big changes.',
        f'{zodiac}, this week has been a struggle, but trust in your tenacity and strength to see the positives come to light',
        f'{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.',
        f'{zodiac}, your ambition will drive you forward this week. Set clear goals and work diligently to achieve them. Success is yours for the taking.',
        f"{zodiac}, your intuition will be your guiding light this week. Trust your inner voice and follow your heart. A spiritual journey awaits you.",
        f"{zodiac}, your innovative ideas will be in high demand this week. Share your unique perspective and inspire others. Change is coming.",
        f"{zodiac}, your passion will be ignited this week. Follow your desires and pursue your dreams with intensity. Success is within reach.",
        f"{zodiac}, balance is key this week. Find harmony between your personal and professional life. A new partnership could be on the horizon.",
        f"{zodiac}, focus on self-care and well-being this week. Take time for yourself to recharge and rejuvenate. Your efforts will pay off.",
        f"{zodiac}, your creativity will shine this week. Express yourself freely and let your talents shine. Recognition is on the horizon.",
        f"{zodiac}, your intuition will be sharp this week. Trust your gut and follow your heart. A new adventure awaits you.",
        f"{zodiac}, expect a whirlwind of activity this week. Be prepared to adapt to changing circumstances and embrace new opportunities.",
        f"{zodiac}, focus on nurturing your relationships this week. Spend quality time with loved ones and strengthen your bonds.",
        f"{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.",
      ]
      
      symbol = "Water-bearer"
      element = "Air"
      quality="Fixed"
      ruler ="Saturn / Uranus"
      detriment = "Sun"
      exalt="Mercury / Neptune"
      fall="Pluto"
      
      
      results = f"""
      [cyan] \u2022 Zodiac symbol: {symbol} \u2022 Zodiac element: {element} \u2022 Zodiac quality: {quality} 
      \u2022 Sign ruler: {ruler} \u2022 Detriment: {detriment} \u2022 Exaltation: {exalt} \u2022 Fall: {fall}[/]
      
      [dark_olive_green2] Backstory [/]:
      Aquarius is one of the three air signs, alongside Gemini and Libra. The ruling planets of Aquarius are Saturn and Uranus.
      The water carrier represented by the constellation Aquarius is Ganymede, a beautiful Phrygian youth. Ganymede was the son of Tros, king of Troy (according to Lucian, he was also the son of Dardanus). While tending to his father's flocks on Mount Ida, Ganymede was spotted by Zeus. 
      
      [dark_olive_green2] Horoscope: [/]
      {random.choice(readings)}
      """
      print(Panel(results, title="Astrology Results", subtitle="Enjoy"))


  def pisces_data(self):

      zodiac="Pisces"
      readings = [
        f"{zodiac}, your adventurous spirit will be calling this week. Explore new horizons and broaden your perspective. A journey awaits you.",
        f'{zodiac}, this season is the time to shine and try out something new, small steps lead to big changes.',
        f'{zodiac}, this week has been a struggle, but trust in your tenacity and strength to see the positives come to light',
        f'{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.',
        f'{zodiac}, your ambition will drive you forward this week. Set clear goals and work diligently to achieve them. Success is yours for the taking.',
        f"{zodiac}, your intuition will be your guiding light this week. Trust your inner voice and follow your heart. A spiritual journey awaits you.",
        f"{zodiac}, your innovative ideas will be in high demand this week. Share your unique perspective and inspire others. Change is coming.",
        f"{zodiac}, your passion will be ignited this week. Follow your desires and pursue your dreams with intensity. Success is within reach.",
        f"{zodiac}, balance is key this week. Find harmony between your personal and professional life. A new partnership could be on the horizon.",
        f"{zodiac}, focus on self-care and well-being this week. Take time for yourself to recharge and rejuvenate. Your efforts will pay off.",
        f"{zodiac}, your creativity will shine this week. Express yourself freely and let your talents shine. Recognition is on the horizon.",
        f"{zodiac}, your intuition will be sharp this week. Trust your gut and follow your heart. A new adventure awaits you.",
        f"{zodiac}, expect a whirlwind of activity this week. Be prepared to adapt to changing circumstances and embrace new opportunities.",
        f"{zodiac}, focus on nurturing your relationships this week. Spend quality time with loved ones and strengthen your bonds.",
        f"{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.",
      ]
      
      symbol = "Fish"
      element = "Water"
      quality="Mutable"
      ruler ="Jupiter"
      detriment = "Mercury"
      exalt="Venus"
      fall="Mercury"
      
      
      results = f"""
      [cyan] \u2022 Zodiac symbol: {symbol} \u2022 Zodiac element: {element} \u2022 Zodiac quality: {quality} 
      \u2022 Sign ruler: {ruler} \u2022 Detriment: {detriment} \u2022 Exaltation: {exalt} \u2022 Fall: {fall}[/]
      
      [dark_olive_green2] Backstory [/]:
      There are no prominent stars in the constellation. One star in the constellation, Alpha Piscium, is also known as Alrescha, Arabic for "the well rope or cord". The constellations in earlier times were primarily used as markers to help determine what influence was in the sky.
      "Pisces" is the [light_sea_green ]Latin word for "fishes"[/]. It is one of the earliest zodiac signs on record, with the two fish appearing as far back as c. 2300 BC on an Egyptian coffin lid. According to one Greek myth, Pisces represents the fish, sometimes represented by a shark.
      
      [dark_olive_green2] Horoscope: [/]
      {random.choice(readings)}
      """
      print(Panel(results, title="Astrology Results", subtitle="Enjoy"))


  def taurus_data(self):

      zodiac="Taurus"
      readings = [
        f"{zodiac}, your adventurous spirit will be calling this week. Explore new horizons and broaden your perspective. A journey awaits you.",
        f'{zodiac}, this season is the time to shine and try out something new, small steps lead to big changes.',
        f'{zodiac}, this week has been a struggle, but trust in your tenacity and strength to see the positives come to light',
        f'{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.',
        f'{zodiac}, your ambition will drive you forward this week. Set clear goals and work diligently to achieve them. Success is yours for the taking.',
        f"{zodiac}, your intuition will be your guiding light this week. Trust your inner voice and follow your heart. A spiritual journey awaits you.",
        f"{zodiac}, your innovative ideas will be in high demand this week. Share your unique perspective and inspire others. Change is coming.",
        f"{zodiac}, your passion will be ignited this week. Follow your desires and pursue your dreams with intensity. Success is within reach.",
        f"{zodiac}, balance is key this week. Find harmony between your personal and professional life. A new partnership could be on the horizon.",
        f"{zodiac}, focus on self-care and well-being this week. Take time for yourself to recharge and rejuvenate. Your efforts will pay off.",
        f"{zodiac}, your creativity will shine this week. Express yourself freely and let your talents shine. Recognition is on the horizon.",
        f"{zodiac}, your intuition will be sharp this week. Trust your gut and follow your heart. A new adventure awaits you.",
        f"{zodiac}, expect a whirlwind of activity this week. Be prepared to adapt to changing circumstances and embrace new opportunities.",
        f"{zodiac}, focus on nurturing your relationships this week. Spend quality time with loved ones and strengthen your bonds.",
        f"{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.",
      ]
      
      symbol = "Bull"
      element = "Earth"
      quality="Fixed"
      ruler ="Venus"
      detriment = "Mars/ Pluto"
      exalt="Moon"
      fall="Uranus"
      
      
      results = f"""
      [cyan] \u2022 Zodiac symbol: {symbol} \u2022 Zodiac element: {element} \u2022 Zodiac quality: {quality} 
      \u2022 Sign ruler: {ruler} \u2022 Detriment: {detriment} \u2022 Exaltation: {exalt} \u2022 Fall: {fall}[/]
      
      [dark_olive_green2] Backstory [/]:
      Taurus is a Venus-ruled sign, the Moon is in its exaltation here at exactly 3°.  Taurus is one of the three earth signs, alongside Capricorn and Virgo. Taurus's opposite sign is Scorpio.
      The bestial sign of Taurus is associated with several myths and bull worship from several ancient cultures. It was the first sign of the zodiac established among the Mesopotamians, who called it "The Great Bull of Heaven," as it was the constellation through which the Sun rose on the vernal equinox at that time. 
      During Taurus, life reaches its full bloom, symbolizing growth and steadfastness.
      
      [dark_olive_green2] Horoscope: [/]
      {random.choice(readings)}
      """
      print(Panel(results, title="Astrology Results", subtitle="Enjoy"))


  def gemini_data(self):

      zodiac="Gemini"
      readings = [
        f"{zodiac}, your adventurous spirit will be calling this week. Explore new horizons and broaden your perspective. A journey awaits you.",
        f'{zodiac}, this season is the time to shine and try out something new, small steps lead to big changes.',
        f'{zodiac}, this week has been a struggle, but trust in your tenacity and strength to see the positives come to light',
        f'{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.',
        f'{zodiac}, your ambition will drive you forward this week. Set clear goals and work diligently to achieve them. Success is yours for the taking.',
        f"{zodiac}, your intuition will be your guiding light this week. Trust your inner voice and follow your heart. A spiritual journey awaits you.",
        f"{zodiac}, your innovative ideas will be in high demand this week. Share your unique perspective and inspire others. Change is coming.",
        f"{zodiac}, your passion will be ignited this week. Follow your desires and pursue your dreams with intensity. Success is within reach.",
        f"{zodiac}, balance is key this week. Find harmony between your personal and professional life. A new partnership could be on the horizon.",
        f"{zodiac}, focus on self-care and well-being this week. Take time for yourself to recharge and rejuvenate. Your efforts will pay off.",
        f"{zodiac}, your creativity will shine this week. Express yourself freely and let your talents shine. Recognition is on the horizon.",
        f"{zodiac}, your intuition will be sharp this week. Trust your gut and follow your heart. A new adventure awaits you.",
        f"{zodiac}, expect a whirlwind of activity this week. Be prepared to adapt to changing circumstances and embrace new opportunities.",
        f"{zodiac}, focus on nurturing your relationships this week. Spend quality time with loved ones and strengthen your bonds.",
        f"{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.",
      ]
      
      symbol = "Twins"
      element = "Air"
      quality="Mutable"
      ruler ="Mercury"
      detriment = "Jupiter"
      exalt="North Node"
      fall="South Node"
      
      
      results = f"""
      [cyan] \u2022 Zodiac symbol: {symbol} \u2022 Zodiac element: {element} \u2022 Zodiac quality: {quality} 
      \u2022 Sign ruler: {ruler} \u2022 Detriment: {detriment} \u2022 Exaltation: {exalt} \u2022 Fall: {fall}[/]
      
      [dark_olive_green2] Backstory [/]:
      Gemini is represented by the twins, Castor and Pollux, known as the Dioscuri in Greek mythology. It is known as a positive, mutable sign.
      In [cyan]Babylonian astronomy[/], the stars Pollux and Castor were known as the Great Twins. Their names were Lugal-irra and Meslamta-ea, meaning "The Mighty King" and "The One who has arisen from the Underworld".
      In [cyan]Greek mythology[/], Gemini is associated with the myth of Castor and Pollux, a pair of twins conceived by different fathers.
      
      [dark_olive_green2] Horoscope: [/]
      {random.choice(readings)}
      """
      print(Panel(results, title="Astrology Results", subtitle="Enjoy"))



  def cancer_data(self):

      zodiac="Cancer"
      readings = [
        f"{zodiac}, your adventurous spirit will be calling this week. Explore new horizons and broaden your perspective. A journey awaits you.",
        f'{zodiac}, this season is the time to shine and try out something new, small steps lead to big changes.',
        f'{zodiac}, this week has been a struggle, but trust in your tenacity and strength to see the positives come to light',
        f'{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.',
        f'{zodiac}, your ambition will drive you forward this week. Set clear goals and work diligently to achieve them. Success is yours for the taking.',
        f"{zodiac}, your intuition will be your guiding light this week. Trust your inner voice and follow your heart. A spiritual journey awaits you.",
        f"{zodiac}, your innovative ideas will be in high demand this week. Share your unique perspective and inspire others. Change is coming.",
        f"{zodiac}, your passion will be ignited this week. Follow your desires and pursue your dreams with intensity. Success is within reach.",
        f"{zodiac}, balance is key this week. Find harmony between your personal and professional life. A new partnership could be on the horizon.",
        f"{zodiac}, focus on self-care and well-being this week. Take time for yourself to recharge and rejuvenate. Your efforts will pay off.",
        f"{zodiac}, your creativity will shine this week. Express yourself freely and let your talents shine. Recognition is on the horizon.",
        f"{zodiac}, your intuition will be sharp this week. Trust your gut and follow your heart. A new adventure awaits you.",
        f"{zodiac}, expect a whirlwind of activity this week. Be prepared to adapt to changing circumstances and embrace new opportunities.",
        f"{zodiac}, focus on nurturing your relationships this week. Spend quality time with loved ones and strengthen your bonds.",
        f"{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.",
      ]
      
      symbol = "Crab"
      element = "Water"
      quality="Cardinal"
      ruler ="Moon"
      detriment = "Saturn"
      exalt="Jupiter"
      fall="Mars"
      
      
      results = f"""
      [cyan] \u2022 Zodiac symbol: {symbol} \u2022 Zodiac element: {element} \u2022 Zodiac quality: {quality} 
      \u2022 Sign ruler: {ruler} \u2022 Detriment: {detriment} \u2022 Exaltation: {exalt} \u2022 Fall: {fall}[/]
      
      [dark_olive_green2] Backstory [/]:
      Cancer is the cardinal sign of the Water trigon, which is made up of Cancer, Pisces, and Scorpio. It is one of the six negative signs, and its ruling planet is the Moon. 
      The sign is most often represented by the crab, based on the Karkinos. Cancer's opposite sign is Capricorn.
      Individuals born during these dates, depending on which system of astrology they subscribe to, may be called "Cancerians". Water is the element associated with Cancer, and, alongside Scorpio and Pisces, it forms the water trigon.
      
      [dark_olive_green2] Horoscope: [/]
      {random.choice(readings)}
      """
      print(Panel(results, title="Astrology Results", subtitle="Enjoy"))


  def leo_data(self):

      zodiac="Leo"
      readings = [
        f"{zodiac}, your adventurous spirit will be calling this week. Explore new horizons and broaden your perspective. A journey awaits you.",
        f'{zodiac}, this season is the time to shine and try out something new, small steps lead to big changes.',
        f'{zodiac}, this week has been a struggle, but trust in your tenacity and strength to see the positives come to light',
        f'{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.',
        f'{zodiac}, your ambition will drive you forward this week. Set clear goals and work diligently to achieve them. Success is yours for the taking.',
        f"{zodiac}, your intuition will be your guiding light this week. Trust your inner voice and follow your heart. A spiritual journey awaits you.",
        f"{zodiac}, your innovative ideas will be in high demand this week. Share your unique perspective and inspire others. Change is coming.",
        f"{zodiac}, your passion will be ignited this week. Follow your desires and pursue your dreams with intensity. Success is within reach.",
        f"{zodiac}, balance is key this week. Find harmony between your personal and professional life. A new partnership could be on the horizon.",
        f"{zodiac}, focus on self-care and well-being this week. Take time for yourself to recharge and rejuvenate. Your efforts will pay off.",
        f"{zodiac}, your creativity will shine this week. Express yourself freely and let your talents shine. Recognition is on the horizon.",
        f"{zodiac}, your intuition will be sharp this week. Trust your gut and follow your heart. A new adventure awaits you.",
        f"{zodiac}, expect a whirlwind of activity this week. Be prepared to adapt to changing circumstances and embrace new opportunities.",
        f"{zodiac}, focus on nurturing your relationships this week. Spend quality time with loved ones and strengthen your bonds.",
        f"{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.",
      ]
      
      symbol = "Lion"
      element = "Fire"
      quality="Fixed"
      ruler ="Sun"
      detriment = "Saturn & Uranus"
      exalt="Pluto"
      fall="Neptune"
      
      
      results = f"""
      [cyan] \u2022 Zodiac symbol: {symbol} \u2022 Zodiac element: {element} \u2022 Zodiac quality: {quality} 
      \u2022 Sign ruler: {ruler} \u2022 Detriment: {detriment} \u2022 Exaltation: {exalt} \u2022 Fall: {fall}[/]
      
      [dark_olive_green2] Backstory [/]:
      Leo is associated with fire, accompanied by Aries and Sagittarius, and its modality is fixed. The constellation Leo is associated with the mythological Nemean lion. The lion is a very important and prominent symbol in Greek mythology
      [cyan]Egyptians[/] worshipped the constellation, which they referred to as "Knem", because it was present during the flooding of the Nile River.
      Egypt, Tutankhamun's gold throne features lion heads where the seat and front legs meet, as well as clawed feet at the end of each leg, symbolizing power and royalty.
      
      [dark_olive_green2] Horoscope: [/]
      {random.choice(readings)}
      """
      print(Panel(results, title="Astrology Results", subtitle="Enjoy"))


  def virgo_data(self):

      zodiac="Virgo"
      readings = [
        f"{zodiac}, your adventurous spirit will be calling this week. Explore new horizons and broaden your perspective. A journey awaits you.",
        f'{zodiac}, this season is the time to shine and try out something new, small steps lead to big changes.',
        f'{zodiac}, this week has been a struggle, but trust in your tenacity and strength to see the positives come to light',
        f'{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.',
        f'{zodiac}, your ambition will drive you forward this week. Set clear goals and work diligently to achieve them. Success is yours for the taking.',
        f"{zodiac}, your intuition will be your guiding light this week. Trust your inner voice and follow your heart. A spiritual journey awaits you.",
        f"{zodiac}, your innovative ideas will be in high demand this week. Share your unique perspective and inspire others. Change is coming.",
        f"{zodiac}, your passion will be ignited this week. Follow your desires and pursue your dreams with intensity. Success is within reach.",
        f"{zodiac}, balance is key this week. Find harmony between your personal and professional life. A new partnership could be on the horizon.",
        f"{zodiac}, focus on self-care and well-being this week. Take time for yourself to recharge and rejuvenate. Your efforts will pay off.",
        f"{zodiac}, your creativity will shine this week. Express yourself freely and let your talents shine. Recognition is on the horizon.",
        f"{zodiac}, your intuition will be sharp this week. Trust your gut and follow your heart. A new adventure awaits you.",
        f"{zodiac}, expect a whirlwind of activity this week. Be prepared to adapt to changing circumstances and embrace new opportunities.",
        f"{zodiac}, focus on nurturing your relationships this week. Spend quality time with loved ones and strengthen your bonds.",
        f"{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.",
      ]
      
      symbol = "Virgin Maiden"
      element = "Earth"
      quality="Mutable"
      ruler ="Mercury"
      detriment = "Jupiter & Neptune"
      exalt="Mercury"
      fall="Venus"
      
      
      results = f"""
      [cyan] \u2022 Zodiac symbol: {symbol} \u2022 Zodiac element: {element} \u2022 Zodiac quality: {quality} 
      \u2022 Sign ruler: {ruler} \u2022 Detriment: {detriment} \u2022 Exaltation: {exalt} \u2022 Fall: {fall}[/]
      
      [dark_olive_green2] Backstory [/]:
      The sign is associated with Astraea, a figure from Greek mythology. Astraea was the last immortal to abandon Earth at the end of the Silver Age when the gods fled to Olympus.
      Virgo is one of the three Earth signs, alongside Capricorn and Taurus. The constellation Virgo has various origins in different mythologies.
      In [cyan]Greek and Roman mythology[/], Virgo is related to Demeter, the Greek goddess of the harvest and autumn, or her daughter Persephone, queen of the Underworld and goddess of spring.
      In [medium_purple1 ]Hindu astrology[/], the comparable sign to Virgo is Kanya, which also means "maiden."
      
      [dark_olive_green2] Horoscope: [/]
      {random.choice(readings)}
      """
      print(Panel(results, title="Astrology Results", subtitle="Enjoy"))


  def libra_data(self):

      zodiac="Libra"
      readings = [
        f"{zodiac}, your adventurous spirit will be calling this week. Explore new horizons and broaden your perspective. A journey awaits you.",
        f'{zodiac}, this season is the time to shine and try out something new, small steps lead to big changes.',
        f'{zodiac}, this week has been a struggle, but trust in your tenacity and strength to see the positives come to light',
        f'{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.',
        f'{zodiac}, your ambition will drive you forward this week. Set clear goals and work diligently to achieve them. Success is yours for the taking.',
        f"{zodiac}, your intuition will be your guiding light this week. Trust your inner voice and follow your heart. A spiritual journey awaits you.",
        f"{zodiac}, your innovative ideas will be in high demand this week. Share your unique perspective and inspire others. Change is coming.",
        f"{zodiac}, your passion will be ignited this week. Follow your desires and pursue your dreams with intensity. Success is within reach.",
        f"{zodiac}, balance is key this week. Find harmony between your personal and professional life. A new partnership could be on the horizon.",
        f"{zodiac}, focus on self-care and well-being this week. Take time for yourself to recharge and rejuvenate. Your efforts will pay off.",
        f"{zodiac}, your creativity will shine this week. Express yourself freely and let your talents shine. Recognition is on the horizon.",
        f"{zodiac}, your intuition will be sharp this week. Trust your gut and follow your heart. A new adventure awaits you.",
        f"{zodiac}, expect a whirlwind of activity this week. Be prepared to adapt to changing circumstances and embrace new opportunities.",
        f"{zodiac}, focus on nurturing your relationships this week. Spend quality time with loved ones and strengthen your bonds.",
        f"{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.",
      ]
      
      symbol = "Scales"
      element = "Air"
      quality="Cardinal"
      ruler ="Venus"
      detriment = "Mars"
      exalt="Saturn"
      fall="Sun"
      
      
      results = f"""
      [cyan] \u2022 Zodiac symbol: {symbol} \u2022 Zodiac element: {element} \u2022 Zodiac quality: {quality} 
      \u2022 Sign ruler: {ruler} \u2022 Detriment: {detriment} \u2022 Exaltation: {exalt} \u2022 Fall: {fall}[/]
      
      [dark_olive_green2] Backstory [/]:
      The symbol of the scales is based on the Scales of Justice held by Themis, the Greek personification of divine law and custom. The ruling planet of Libra is Venus along with Taurus.
      Libra is the cardinal modality of the three air signs, the others being Gemini and Aquarius. Libra is symbolized by the scales and is associated with the Roman deity Iustitia. 
      
      
      [dark_olive_green2] Horoscope: [/]
      {random.choice(readings)}
      """
      print(Panel(results, title="Astrology Results", subtitle="Enjoy"))


  def scorpio_data(self):

      zodiac="Scorpio"
      readings = [
        f"{zodiac}, your adventurous spirit will be calling this week. Explore new horizons and broaden your perspective. A journey awaits you.",
        f'{zodiac}, this season is the time to shine and try out something new, small steps lead to big changes.',
        f'{zodiac}, this week has been a struggle, but trust in your tenacity and strength to see the positives come to light',
        f'{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.',
        f'{zodiac}, your ambition will drive you forward this week. Set clear goals and work diligently to achieve them. Success is yours for the taking.',
        f"{zodiac}, your intuition will be your guiding light this week. Trust your inner voice and follow your heart. A spiritual journey awaits you.",
        f"{zodiac}, your innovative ideas will be in high demand this week. Share your unique perspective and inspire others. Change is coming.",
        f"{zodiac}, your passion will be ignited this week. Follow your desires and pursue your dreams with intensity. Success is within reach.",
        f"{zodiac}, balance is key this week. Find harmony between your personal and professional life. A new partnership could be on the horizon.",
        f"{zodiac}, focus on self-care and well-being this week. Take time for yourself to recharge and rejuvenate. Your efforts will pay off.",
        f"{zodiac}, your creativity will shine this week. Express yourself freely and let your talents shine. Recognition is on the horizon.",
        f"{zodiac}, your intuition will be sharp this week. Trust your gut and follow your heart. A new adventure awaits you.",
        f"{zodiac}, expect a whirlwind of activity this week. Be prepared to adapt to changing circumstances and embrace new opportunities.",
        f"{zodiac}, focus on nurturing your relationships this week. Spend quality time with loved ones and strengthen your bonds.",
        f"{zodiac}, your energy levels will be high. Take advantage of this to tackle new challenges and pursue your goals with passion.",
      ]
      
      symbol = "Scorpion"
      element = "Water"
      quality="Fixed"
      ruler ="Mars"
      detriment = "Venus"
      exalt="Uranus"
      fall="Moon"
      
      
      results = f"""
      [cyan] \u2022 Zodiac symbol: {symbol} \u2022 Zodiac element: {element} \u2022 Zodiac quality: {quality} 
      \u2022 Sign ruler: {ruler} \u2022 Detriment: {detriment} \u2022 Exaltation: {exalt} \u2022 Fall: {fall}[/]
      
      [dark_olive_green2] Backstory [/]:
      Scorpio is one of the water signs, the others being Cancer and Pisces. It is a fixed, negative sign.
      According to [cyan]Greek mythology[/], its representation as a scorpion is related to the Greek legend of Orion and how a scorpion stung him to death (said to be why Orion sets as Scorpius rises in the sky).
      Another Greek myth recounts how a scorpion caused the horses of the Sun to bolt, when they were being driven by the inexperienced youth, Phaethon.
      
      [dark_olive_green2] Horoscope: [/]
      {random.choice(readings)}
      """
      print(Panel(results, title="Astrology Results", subtitle="Enjoy"))


  def progressbar(self):
    import time
    from rich.progress import track
    from rich.progress import Progress

    print('\n')
    for i in track(range(10), description="[dark_olive_green2 ]Getting Astrology data ...[/]"):
        time.sleep(0.5)  # Simulate work being done 
    

    with Progress() as progress:

        # task1 = progress.add_task("[thistle3 ] Downloading...", total=600)
        task2 = progress.add_task("[green] Processing...", total=500)
        task3 = progress.add_task("[purple3] Astrology stuff ...", total=500)

        while not progress.finished:
            # progress.update(task1, advance=0.9)
            progress.update(task2, advance=1)
            progress.update(task3, advance=0.7)
            time.sleep(0.02)
      
    # retro2()
      
    
  

def zodiac():
  
  print('\n')
  
  # Astrology Signs class 
  s = Signs()
  
  # Error handling try-except
  try: 
    bullet = "\u2022"
    # w2 = "[misty_rose1 ] Astrology is the stuff people believe in that determines outcomes in their lives.[/]\n Enter all of your personal data below to get started"
    w2 = f"""[misty_rose1 ]Astrological belief in relation between celestial observations and terrestrial events have influenced various aspects of human history, including world-views, language and many elements of culture. [cyan]Babylonian astrology[/] is the earliest recorded organized system of astrology, arising in the 2nd millennium BC. [/]
    
    Astrology has history in: 
    {bullet} Babylonia {bullet} Greece & Rome {bullet} Islamic World {bullet} India {bullet} China
    
    [misty_rose1 ] Enter your Astrology information below to get started [/]
    """
    
    print(Panel(w2, title="Welcome to AstrologyPy", subtitle=""))

    console.print("[blue_violet ] Enter your month of birth (1 to 12) [/]")
    birth_month = int(input(" month: "))
    console.print("[dark_goldenrod ] Enter your day of birth (1 to 31) [/]")
    birth_day = int(input(" day: "))
    
    if birth_month <1 :
      print("[red] Invalid! [/]")
      return TypeError
    if birth_day<1:
      print("[red] Invalid! [/]")
      return TypeError
    else:


      if birth_month == 1:
        if birth_day not in s.capricorn_jan :
          # print(" not Capricorn birthday ")
          if birth_day in s.aquarius_jan :
            print(f" {s.aquarius} [deep_pink2 ]Aquarious[/] birthday in January: {s.aquarius_jan[::2]}")
            s.progressbar()
            s.aquarius_data()
        else:
          print(f" {s.capricorn} [deep_pink2 ]Capricorn[/] birthday in January: {s.capricorn_jan[::4]}")
          s.progressbar()
          s.capricorn_data()
          
          
      if birth_month == 2:
        if birth_day not in s.aquarius_feb:
          # print("not aquarius")
          if birth_day in s.pisces_feb:
            print(f" {s.pisces} [light_pink3 ]Pisces[/] birthday in February: {s.pisces_feb[::2]}")
            s.progressbar()
            s.pisces_data()
        else:
          print(f" {s.aquarius} [light_pink3 ]Aquarious[/] birthday in Feburary: {s.aquarius_feb[::2] }")
          s.progressbar()
          s.aquarius_data()
          
          
      if birth_month == 3:
        if birth_day not in s.pisces_march:
          # print("not pisces march")
          if birth_day in s.aries_march:
            print(f" {s.aries} [deep_pink2 ]Aries[/] birthday in March: {s.aries_march[::2]}")
            s.progressbar()
            s.aries_data()
        else:
          print(f" {s.pisces} [light_pink3 ]Pisces[/] birthday in March: {s.pisces_march[::2] }")
          s.progressbar()
          s.pisces_data()
          
          
      if birth_month == 4:
        if birth_day not in s.aries_april:
          if birth_day in s.taurus_april:
            print(f" {s.taurus} [medium_purple1 ]Taurus[/] birthday in April: {s.taurus_april[::2]}")
            s.progressbar()
            s.taurus_data()
            
        else:
          print(f" {s.aries} [deep_pink2 ]Aries[/] birthday in April: {s.aries_april[::2]}")
          s.progressbar()
          s.aries_data()


      if birth_month == 5:
        if birth_day not in s.gemini_may:
          if birth_day in s.taurus_may:
            print(f" {s.taurus} [medium_purple1 ]Taurus[/] birthday in May : {s.taurus_may[::5]}")
            s.progressbar()
            s.taurus_data()
        else:
          print(f" {s.gemini} [dark_goldenrod ]Gemini[/] birthday in May: {s.gemini_may[::2]}")
          s.progressbar()
          s.gemini_data()


      if birth_month == 6:
        if birth_day not in s.gemini_june:
          if birth_day in s.cancer_june:
            print(f" {s.cancer} [deep_pink2 ]Cancer[/] birthday in June: {s.cancer_june[::2]}")
            s.progressbar()
            s.cancer_data()
            
        else:
          print(f" {s.gemini} [dark_goldenrod ]Gemini[/] birthday in June: {s.gemini_june[::2]}")
          s.progressbar()
          s.gemini_data()


      if birth_month == 7:
        if birth_day not in s.cancer_july:
          if birth_day in s.leo_july:
            print(f" {s.leo} [dark_olive_green2 ]Leo birthday[/] in July: {s.leo_july[::4]}")
            s.progressbar()
            s.leo_data()
            
        else:
          print(f" {s.cancer} [deep_pink2 ]Cancer[/] birthday in July: {s.cancer_july[::2]}")
          s.progressbar()
          s.cancer_data()


      if birth_month == 8:
        if birth_day not in s.leo_aug:
          # print("not Aries april")
          if birth_day in s.virgo_aug:
            print(f" {s.virgo} [light_pink3 ]Virgo[/] birthday August: {s.virgo_aug[::2]}")
            s.progressbar()
            s.virgo_data()
            
        else:
          print(f" {s.leo} [dark_olive_green2 ]Leo[/] birthday in August: {s.leo_aug[::4]}")
          s.progressbar()
          s.leo_data()
        


      if birth_month == 9:
        if birth_day not in s.libra_sept:
          if birth_day in s.virgo_sept:
            print(f" {s.virgo} [light_pink3 ]Virgo[/] birthday in September: {s.virgo_sept[::4]}")
            s.progressbar()
            s.virgo_data()
        else:
          print(f" {s.libra} [light_pink3 ]Libra[/] birthday in September: {s.libra_sept[::2]}")
          s.progressbar()
          s.libra_data()


      if birth_month == 10:
        if birth_day not in s.libra_oct:
          if birth_day in s.scorpio_oct:
            print(f" {s.scorpio} [light_sea_green ]Scorpio[/] birthday in October: {s.scorpio_oct[::2]}")
            s.progressbar()
            s.scorpio_data()
            
        else:
          print(f" {s.libra} [light_pink3 ]Libra[/] birthday in October: {s.libra_oct[::4]}")
          s.progressbar()
          s.libra_data()


      if birth_month == 11:
        if birth_day not in s.scorpio_nov:
          # print("not Aries april")
          if birth_day in s.Sagittarius_nov:
            print(f" {s.Sagittarius} [indian_red ]Sagittarius[/] birthday in November: {s.Sagittarius_nov[::2]}")
            s.progressbar()
            s.Sagittarius_data()
        else:
          print(f" {s.scorpio} [light_sea_green ]Scorpio[/] birthday in November: {s.scorpio_nov[::4]}")
          s.progressbar()
          s.scorpio_data()


      if birth_month == 12:
        if birth_day not in s.capricorn_dec:
          # print("not capricorn dec")
          if birth_day in s.Sagittarius_dec:
            print(f" {s.Sagittarius} [indian_red ]Sagittarius[/] birthday in December: {s.Sagittarius_dec[::4] }")
            s.progressbar()
            s.Sagittarius_data()
            
        else:
          print(f" {s.capricorn} [indian_red ]Capricorn[/] birthday in January: {s.capricorn_dec[::2] }")
          s.progressbar()
          s.capricorn_data()
        
    
  # if invalid input return function  
  except ValueError:
    
    print(" >>> Enter a valid integer (1-12)")
    zodiac()




if __name__ == "__main__":
  zodiac()









