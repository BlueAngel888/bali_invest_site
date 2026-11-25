#!/usr/bin/env python3
# Builds site/index.html for the Bali Invest Nuanu presentation site.
import html, urllib.parse, os

WA_NUM = "40757070757"
WA_DISPLAY = "+40 757 070 757"
EMAIL = "baliinvestrealestate@gmail.com"

def wa(msg):
    return f"https://wa.me/{WA_NUM}?text=" + urllib.parse.quote(msg)

def e(s):
    return html.escape(s, quote=True)

# ---------- Nuanu projects (source: partners.nuanu.realestate, Nov 2026) ----------
NUANU = [
  dict(id="luna", beds="S,1,2,3", name="Luna Residences", dev="618 Development", tags=["apartments","beachfront","offplan"],
       kind="Beachfront residences", price="$185,000", handover="Q4 2028", own="Leasehold 60+ years", roi="10–14%",
       units="Studio to 3BR penthouse",
       about="A beachfront residential project where the river meets the ocean, part of the Nuanu Creative City ecosystem. Ocean-view residences with private terraces, full blackout systems, YODEZEEN-designed interiors and panoramic views of the ocean, river and jungle. From 25% down payment.",
       amen=["Luna Beach Club access","Private ocean beach","YODEZEEN interiors","5-star 24/7 property management","In-residence dining","Daily shuttle in Nuanu","Lumeira Spa nearby","International school nearby"],
       imgs=["luna-residences_6","luna-residences_3","luna-residences_4","luna-residences_7","luna-residences_5","luna-residences_8"], vid="luna"),
  dict(id="flower", beds="2,3", name="Flower Estates", dev="618 Development", tags=["villas","freehold","offplan"],
       kind="Standalone villas, 2–3 BR", price="$500,000", handover="Q3 2027", own="Freehold for foreigners", roi="10–12%",
       units="26 standalone villas",
       about="The first residential project on Nuanu's Golden Mile, the most exclusive district of the city. Standalone villas only, each with its own signature plant in a private garden. No apartment blocks, no hotels.",
       amen=["Communal flower gardens","Flower shop","Juice bar","Tea lounge","Fire pit & BBQ area","Kids' playground","Pedestrian-friendly walkways"],
       imgs=["flower-estates_1","flower-estates_8","flower-estates_2","flower-estates_4","flower-estates_6","flower-estates_3"], vid="flower"),
  dict(id="pavilions", beds="3,4,5", name="The Pavilions", dev="OXO Living", tags=["villas","freehold","offplan"],
       kind="Pavilion-style villas", price="$620,000", handover="Q3 2027", own="Freehold for foreigners", roi=None,
       units="26 boutique villas",
       about="An exclusive boutique development of pavilion-style villas co-created by OXO Living and Precht. Inspired by traditional Balinese pavilion living, it is built around privacy, wellness and longevity, with a private wellness center for owners.",
       amen=["Private wellness center “The Core”","Meditation pyramid","Hammam & saunas","Hydrotherapy indoor pools","Gym & yoga studio","Sound healing","Café “Nowhere”"],
       imgs=["the-pavilions_1","the-pavilions_8","the-pavilions_2","the-pavilions_3","the-pavilions_5","the-pavilions_9"], vid="pavilions"),
  dict(id="xhotel", beds="S", name="X Hotel", dev="Nuanu & Rentaved", tags=["hotel","offplan"],
       kind="Investment hotel rooms", price="$173,999", handover="2027", own="Leasehold 25 + 20 years", roi="10–14%",
       units="41 hotel rooms",
       about="The first investment hotel inside Nuanu Creative City and its official hospitality partner: a 4-star property 3 minutes from the beach. Bali's first art-experience hotel concept, with recycled art façade panels, light-mapping installations, the largest natural lagoon pool in Nuanu and a 360° sunset rooftop. About 30% of 2027 bookings are pre-confirmed.",
       amen=["45 m lagoon pool (420 m²)","360° rooftop bar","On-site restaurant","Hotel gym","24/7 concierge","Private balconies in every room","Experience Concierge"],
       imgs=["xhotel_6","xhotel_4","xhotel_1","xhotel_3","xhotel_2","xhotel_7"], vid="xhotel"),
  dict(id="bso", beds="S,1,2,3,4", name="Black Sands Oasis", dev="UNIT (Unit Space)", tags=["villas","apartments","offplan"],
       kind="Villas, studios & penthouses", price="$115,400", handover="2028", own="Leasehold 35 + 20 years", roi="10.5–17.8%",
       units="83 villas · 20 studios · 8 penthouses",
       about="A 1.5-hectare development 700 m from the ocean that fuses desert-modern architecture with Moroccan, dune-inspired aesthetics, surrounded by 5 hectares of landscaped walking areas. Apartments are scheduled for April 2028 and villas for October 2028.",
       amen=["Hammam","Reflection pool","Arabic-cuisine restaurant","Rooftop area","Direct access to Aurora Park","30+ restaurants within 1 min","International school & kindergarten (1 min)"],
       imgs=["black-sands-oasis_5","black-sands-oasis_1","black-sands-oasis_3","black-sands-oasis_2","black-sands-oasis_8","black-sands-oasis_9"], vid="bso"),
  dict(id="biom", beds="S,1,2,3", name="BIOM", dev="Biom Development Group", tags=["villas","apartments","freehold","offplan"],
       kind="Villas & residences", price="$145,000", handover="Q4 2027", own="Leasehold 35 + 20 years · freehold for 2–3 BR villas", roi="12–14%",
       units="Living district by Rustam Kerimov",
       about="A nature-integrated living district designed by architect Rustam Kerimov, 400 m from the ocean. Developed with Nuanu and Atom Group, close to international schools and kindergartens, made for families and professionals.",
       amen=["Swimming pools","Clubhouse & café","Yoga shala","Co-working","Outdoor fitness zone","Playgrounds & gardens","24/7 check-in & rental management"],
       imgs=["biom_3","biom_1","biom_5","biom_9","biom_4","biom_7"], vid="biom"),
  dict(id="origins", beds="2,3,4", name="Origins", dev="Bali Baza Development", tags=["villas","hotel","offplan"],
       kind="Boutique hotel villas", price="$590,700", handover="Q2 2027", own="Leasehold 35 years", roi="14–15%",
       units="18 one-of-a-kind villas",
       about="A collection of boutique villas in a soft-brutalism style that runs as a premium boutique hotel with professional management. Volcanic stone, warm timber, sweeping arched windows and private pools in tropical gardens. Each villa has its own character in the Character Hotel format.",
       amen=["Private pools","Rooftop terrace with grill","Cabana, yoga deck & koi pond","Electric scooter per villa","Starlink internet","24/7 luxury concierge","Destination restaurant & lounge"],
       imgs=["origins_8","origins_1","origins_2","origins_3","origins_6","origins_9"], vid="origins"),
  dict(id="ecoverse", beds="S,2,3", name="Ecoverse Residences", dev="NPG Indonesia", tags=["apartments","ready"],
       kind="Eco-luxury residences", price="$197,000", handover="Completed (Q1 2026)", own="Leasehold 25 + 30 years priority extension", roi="11–15%",
       units="Ready to move in",
       about="Eco-friendly luxury living that pairs environmental responsibility with high construction standards. Completed in Q1 2026, with a 25-year structural warranty and a 1-year interior warranty, managed by OXO.",
       amen=["Olympic pool","Modern gym","Co-working & meeting room","Restaurant","24/7 reception","Solar panels","UV water filters","Underground parking"],
       imgs=["ecoverse_5","ecoverse_1","ecoverse_8","ecoverse_3","ecoverse_9","ecoverse_7"], vid="ecoverse"),
  dict(id="vol1", beds="3", name="The Collections Vol. 1", dev="618 Development", tags=["villas","ready"],
       kind="Japandi pool villas", price="$750,000", handover="Completed (Q4 2025)", own="Leasehold 24 years, renewable to 34", roi="13.7%",
       units="Villa collection",
       about="A villa complex with ocean views, 300 m from the beach and 10 minutes from Canggu. Japandi architecture, with construction details made for Bali's humid climate, including enhanced waterproofing of foundations, walls and roofs.",
       amen=["Private pool & terrace","Landscaped garden","250 m to the ocean","Full property management","Access to Nuanu infrastructure"],
       imgs=["collectionsvol1_4","collectionsvol1_3","collectionsvol1_7","collectionsvol1_8","collectionsvol1_9","collectionsvol1_6"], vid="vol1"),
  dict(id="vol2", beds="3", name="The Collections Vol. 2", dev="618 Development", tags=["villas","freehold"],
       kind="Grand private villas", price="$1,050,000", handover="Q4 2026", own="Freehold for foreigners", roi="11–12%",
       units="Villa collection",
       about="Grand private villas inside Nuanu Creative City, 10 minutes' walk to the beach and 10 minutes' drive to Canggu, managed by Nuanu. Built for the tropical climate, with enhanced waterproofing throughout.",
       amen=["Private pool & deck","Landscaped garden","10 min walk to the beach","Full property management"],
       imgs=["collectionsvol2_6","collectionsvol2_3","collectionsvol2_2","collectionsvol2_7","collectionsvol2_8","collectionsvol2_9"], vid="vol2"),
  dict(id="vol3", beds="5", name="The Collections Vol. 3", dev="618 Development", tags=["villas","freehold"],
       kind="Signature 5-bedroom villas", price="$1,800,000", handover="Q3 2026", own="Freehold for foreigners", roi=None,
       units="2 signature villas",
       about="The signature villa collection by 618 Development: open-plan living, floor-to-ceiling panoramic windows and views over a banana grove, in the heart of Nuanu.",
       amen=["Banana grove views","Open-plan living","Floor-to-ceiling windows","Nature-integrated design"],
       imgs=["collectionsvol3_7","collectionsvol3_2","collectionsvol3_6","collectionsvol3_8","collectionsvol3_5","collectionsvol3_9"], vid="vol3"),
  dict(id="residence", beds="3,4,5", name="The Residence", dev="OXO Living", tags=["villas","freehold"],
       kind="Family villas", price="$685,110", handover="Q4 2026", own="Freehold for foreigners", roi=None,
       units="Villa community",
       about="Spacious, carefully crafted villas for living and investment by OXO Living, available on freehold terms to Indonesian and international buyers.",
       amen=["Clubhouse","Kids pool","Playground","BBQ area","24/7 security"],
       imgs=["the-residence_5","the-residence_3","the-residence_8","the-residence_9","the-residence_6","the-residence_7"], vid="residence"),
  dict(id="nyanyi", beds="S,2", name="Nyanyi Village U3", dev="UNIT (Unit Space)", tags=["apartments","villas"],
       kind="Family village", price="$118,700", handover="Q3 2026", own="Leasehold 25 + 25 years priority extension", roi="12–22%",
       units="Next to Pro Education school",
       about="A family-friendly village by Unit Space Group, right next to Pro Education International School and a kindergarten. The developer states a guaranteed minimum 9% return in the first year.",
       amen=["Pro Education International School","Kindergarten from age 3","Children's room with caregiver","Creative workshops & festivals","Family community"],
       imgs=["nyanyi-village-u3_3","nyanyi-village-u3_1","nyanyi-village-u3_8","nyanyi-village-u3_4","nyanyi-village-u3_5","nyanyi-village-u3_6"], vid="nyanyi"),
  dict(id="u2", beds="S,1,2,3", name="Unit Nuanu Village", dev="UNIT (Unit Space)", tags=["apartments","villas","ready"],
       kind="Apartments & villas", price=None, handover="Completed", own="Leasehold", roi=None,
       units="Rice field views",
       about="The cornerstone of Unit Space Village, the first phase of Unit Space City. Finished apartments and villas with rice field views, inside the Nuanu ecosystem.",
       amen=["Schools & kindergartens nearby","Low-rise living","Green spaces","Nuanu City infrastructure"],
       imgs=["unit-nuanu-u2x_1","unit-nuanu-u2_1","unit-nuanu-u2x_2","unit-nuanu-u2x_3","unit-nuanu-u2x_4","unit-nuanu-u2x_5","unit-nuanu-u2x_6","unit-nuanu-u2x_7","unit-nuanu-u2x_8","unit-nuanu-u2x_9","unit-nuanu-u2_2"], vid="u2"),
  dict(id="u1", beds="S,1,2", name="Unit Space U1", dev="UNIT (Unit Space)", tags=["apartments","villas","ready"],
       kind="Low-rise village", price=None, handover="Completed", own="Leasehold", roi=None,
       units="Lived-in community",
       about="The first village of Unit Space City: completed and lived in, with low-rise homes, green spaces and a real community around you in Nuanu.",
       amen=["Low-rise homes","Green spaces","Schools & kindergartens nearby","Nuanu City infrastructure"],
       imgs=["unit-space-u1x_1","unit-space-u1_4","unit-space-u1x_2","unit-space-u1x_3","unit-space-u1x_4","unit-space-u1x_5","unit-space-u1x_6","unit-space-u1x_7","unit-space-u1x_8","unit-space-u1_1"], vid="u1"),
]

# ---------- BREIG Property (public listings: rumavi.com, realting.com, lazudi.com) ----------
BREIG = [
  dict(id="edem2", beds="S,1,2,3", name="Edem Villas II", area="Nusa Dua · Benoa", price="$102,000", kind="Studios to 3BR villas, 24–180 m²",
       handover="Q4 2027 (off-plan)", own="Leasehold up to 60 years",
       about="Furnished, turnkey units 500 m from the ocean in the Nusa Dua tourism zone, with smart-home tech and solar energy. Rental programme with Homes & Villas by Marriott. Payment plan: 15% + 15%, then 0% instalments during construction.",
       amen=["Private pools (villas)","Rooftop terraces","Gym, sauna & spa","Yoga & co-working","Restaurant","Kids zone"],
       imgs=["breig-edem_1","breig-edem_5","breig-edem_3","breig-edem_2"]),
  dict(id="garden2", beds="3", name="Garden Villa II", area="Sukawati · Gianyar", price="$330,000", kind="3BR jungle villas, ~180 m²",
       handover="Completed (Q4 2025)", own="Leasehold",
       about="A boutique complex of four jungle villas on the southern edge of the Ubud corridor, with rice-field and jungle views, 20 minutes from Sanur and Ubud.",
       amen=["Jungle infinity pool","Rice-field views","Garden & balcony","BBQ area","Managed rental"],
       imgs=["breig-garden_5","breig-garden_3","breig-garden_4","breig-garden_1"]),
  dict(id="aqua1", beds="3,4", name="Aquamarine I", area="Berawa · Canggu", price="$620,000", kind="3–4BR pool villas, 263–358 m²",
       handover="Completed", own="Leasehold",
       about="Private-pool villas 200 m from Nelayan Beach, close to Atlas and Finns beach clubs. Rooftop terraces, sauna and smart-home features in selected villas.",
       amen=["Private pool","Rooftop terrace","Sauna (selected)","Smart home","Managed rental"],
       imgs=["breig-aqua_1","breig-aqua_2","breig-aqua_3","breig-aqua_4"]),
  dict(id="baliwood2", beds="3,4,5", name="Baliwood II", area="Pererenan · Canggu", price="$750,000", kind="3–5BR oceanfront villas, 268–336 m²",
       handover="Completed", own="Leasehold",
       about="Luxury villas a one-minute walk from Pererenan Beach, with ocean views from the rooftop terraces, 10 minutes from Canggu.",
       amen=["Private pool","Rooftop with ocean views","Garden & balcony","BBQ area","Managed rental"],
       imgs=["breig-baliwood_2","breig-baliwood_1","breig-baliwood_3","breig-baliwood_5"]),
]

TAG_LABEL = dict(villas="Villas", apartments="Apartments", hotel="Hotel", freehold="Freehold", ready="Ready", offplan="Off-plan", beachfront="Beachfront")

def pic(name, alt, sizes="(min-width: 1000px) 60vw, 100vw", cls="", eager=False, zoom=True, gal=None, idx=0):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    z = f' data-zoom="media/img/{name}.webp"' if zoom else ""
    if gal: z += f' data-gal="{gal}" data-idx="{idx}"'
    return (f'<img class="{cls}" src="media/img/{name}-s.webp" '
            f'srcset="media/img/{name}-s.webp 800w, media/img/{name}.webp 1600w" sizes="{sizes}" '
            f'alt="{e(alt)}" {load} decoding="async"{z}>')

BUBBLE = '<img class="face" src="media/img/florin-s.webp" srcset="media/img/florin-s.webp 1x, media/img/florin.webp 2x" alt="Florin, Bali Invest" width="64" height="64" loading="lazy">'

def cta_band(title, msg, i):
    return f'''
<aside class="cta-band" aria-label="Contact Florin">
  <div class="wrap cta-inner">
    <img class="face big" src="media/img/florin.webp" alt="Florin, Bali Invest" width="120" height="120" loading="lazy">
    <div class="cta-copy">
      <p class="eyebrow">Bali Invest · Florin</p>
      <h3>{e(title)}</h3>
      <p class="cta-sub">Brochures, layouts, price lists and video tours on WhatsApp. Usually within the same day.</p>
    </div>
    <div class="cta-actions">
      <a class="btn wa" href="{wa(msg)}" target="_blank" rel="noopener">{WA_ICON}<span>Ask for details</span></a>
      <span class="num mono">{WA_DISPLAY}</span>
    </div>
  </div>
</aside>'''

WA_ICON = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.9 9.9 0 0 0 4.74 1.21h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2Zm0 18.15h-.01a8.23 8.23 0 0 1-4.19-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.38c0-4.54 3.7-8.23 8.25-8.23 2.2 0 4.27.86 5.82 2.42a8.18 8.18 0 0 1 2.41 5.82c0 4.54-3.7 8.23-8.23 8.23Zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.13-.16.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.01-.38.11-.51.11-.11.25-.29.37-.43.13-.15.17-.25.25-.42.08-.16.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.22.25-.86.85-.86 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.23 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.08.14-1.18-.06-.1-.22-.16-.47-.28Z"/></svg>'

def beds_label(b):
    parts = ["Studio" if x == "S" else x for x in b.split(",")]
    if parts == ["Studio"]:
        return "Studio / hotel room"
    nums = [x for x in parts if x != "Studio"]
    lab = (" · ".join(nums) + " bedrooms") if len(nums) > 1 else (nums[0] + (" bedroom" if nums[0] == "1" else " bedrooms"))
    return ("Studio · " if "Studio" in parts else "") + lab

def beds_attr(b):
    return " ".join("b" + x.lower() for x in b.split(","))

def gallery(gid, imgs, alt, first_cls, first_sizes, thumb_cls, thumb_sizes, max_thumbs):
    main = pic(imgs[0], alt, sizes=first_sizes, cls=first_cls, gal=gid, idx=0)
    rest = imgs[1:]
    shown = rest[:max_thumbs]
    more = len(rest) - len(shown)
    lis = []
    for j, im in enumerate(shown, 1):
        badge = f'<span class="more" aria-hidden="true">+{more}</span>' if (j == len(shown) and more > 0) else ''
        lis.append(f'<li>{pic(im, alt + " photo " + str(j + 1), sizes=thumb_sizes, gal=gid, idx=j)}{badge}</li>')
    hidden = "".join(f'<span hidden data-gal="{gid}" data-idx="{k}" data-zoom="media/img/{im}.webp" data-alt="{e(alt)} photo {k + 1}"></span>'
                     for k, im in enumerate(rest[len(shown):], len(shown) + 1))
    return main, f'<ul class="thumbs {thumb_cls}">{"".join(lis)}</ul>{hidden}'

def fact(label, value, note=False):
    if not value: return ""
    star = '<sup>*</sup>' if note else ''
    return f'<div class="fact"><dt>{e(label)}</dt><dd>{e(value)}{star}</dd></div>'

def project_section(p, n):
    price = p["price"] or "On request"
    tags = "".join(f'<span class="tag">{TAG_LABEL[t]}</span>' for t in p["tags"])
    imgs = p["imgs"]
    main, thumbs = gallery(p["id"], imgs, f'{p["name"]}, Nuanu Bali', "g-main", "(min-width: 1000px) 60vw, 100vw", "", "(min-width: 1000px) 15vw, 33vw", 5)
    amen = "".join(f"<li>{e(a)}</li>" for a in p["amen"])
    msg = f"Hello Florin, I'd like details about {p['name']} in Nuanu, Bali (brochure, layouts, prices)."
    video = ""
    if p.get("vid"):
        video = f'''
      <figure class="phone">
        <video controls playsinline preload="none" poster="media/v/{p["vid"]}.webp" aria-label="Video tour: {e(p["name"])}">
          <source src="media/v/{p["vid"]}.mp4" type="video/mp4">
        </video>
        <figcaption class="mono">Video tour · tap to play</figcaption>
      </figure>'''
    return f'''
<section class="project" id="{p["id"]}" data-tags="{' '.join(p['tags'])}" data-beds="{beds_attr(p['beds'])}">
  <div class="wrap">
    <header class="p-head">
      <p class="p-index mono">{n:02d} / {len(NUANU):02d} · Nuanu</p>
      <h2>{e(p["name"])}</h2>
      <p class="p-kind">{e(p["kind"])} · by {e(p["dev"])}</p>
      <div class="tags">{tags}</div>
    </header>
    <div class="p-grid">
      <div class="gallery">
        {main}
        {thumbs}
      </div>
      <div class="p-info">
        <p class="price">{'<span class="from mono">from</span> ' if p["price"] else ''}{e(price)}</p>
        <dl class="facts">
          {fact("Bedrooms", beds_label(p["beds"]))}
          {fact("Handover", p["handover"])}
          {fact("Ownership", p["own"])}
          {fact("Project", p["units"])}
          {fact("Projected yield", p["roi"], note=True)}
        </dl>
        <p class="about">{e(p["about"])}</p>
        <ul class="amen">{amen}</ul>
        <div class="ask">
          {BUBBLE}
          <a class="btn wa" href="{wa(msg)}" target="_blank" rel="noopener">{WA_ICON}<span>Ask Florin about {e(p["name"])}</span></a>
        </div>
      </div>
      {video}
    </div>
  </div>
</section>'''

def breig_card(b):
    amen = "".join(f"<li>{e(a)}</li>" for a in b["amen"])
    main, thumbs = gallery(b["id"], b["imgs"], b["name"] + " by BREIG", "b-main", "(min-width: 1000px) 45vw, 100vw", "small", "(min-width: 1000px) 12vw, 30vw", 3)
    msg = f"Hello Florin, I'd like details about {b['name']} by BREIG ({b['area']}, Bali)."
    return f'''
<article class="b-card" id="{b["id"]}" data-tags="villas" data-beds="{beds_attr(b['beds'])}">
  {main}
  {thumbs}
  <div class="b-body">
    <p class="eyebrow">{e(b["area"])}</p>
    <h3>{e(b["name"])}</h3>
    <p class="price sm"><span class="from mono">from</span> {e(b["price"])}</p>
    <dl class="facts">
      {fact("Bedrooms", beds_label(b["beds"]))}
      {fact("Type", b["kind"])}
      {fact("Status", b["handover"])}
      {fact("Ownership", b["own"])}
    </dl>
    <p class="about">{e(b["about"])}</p>
    <ul class="amen">{amen}</ul>
    <div class="ask">{BUBBLE}<a class="btn wa" href="{wa(msg)}" target="_blank" rel="noopener">{WA_ICON}<span>Ask about {e(b["name"])}</span></a></div>
  </div>
</article>'''

def index_card(p, n):
    price = p["price"] or "On request"
    return f'''<li class="ix" data-tags="{' '.join(p['tags'])}" data-beds="{beds_attr(p['beds'])}"><a href="#{p["id"]}">
  {pic(p["imgs"][0], p["name"], sizes="(min-width: 1000px) 22vw, 50vw", zoom=False)}
  <span class="ix-meta"><span class="ix-name">{e(p["name"])}</span><span class="ix-price mono">{'from ' if p["price"] else ''}{e(price)}</span><span class="ix-beds">{e(beds_label(p["beds"]))}</span></span></a></li>'''

sections = []
for i, p in enumerate(NUANU, 1):
    sections.append(project_section(p, i))
    if i in (3, 7, 11):
        nxt = NUANU[i]["name"] if i < len(NUANU) else "Nuanu"
        titles = {3: "Like what you see? I'll send you the full presentation.",
                  7: "Comparing projects? I can put them side by side for you.",
                  11: "Want a video call or an on-site viewing in Bali?"}
        sections.append(cta_band(titles[i], f"Hello Florin, I saw your Nuanu projects page and I'd like more details.", i))

bed_filters = "".join(f'<button type="button" class="chip bchip" data-b="{k}" id="fb-{k}" aria-pressed="false">{v}</button>' for k, v in [("bs","Studio"),("b1","1 BR"),("b2","2 BR"),("b3","3 BR"),("b4","4 BR"),("b5","5 BR")])
filters = "".join(f'<button type="button" class="chip" data-f="{k}" id="f-{k}" aria-pressed="false">{v}</button>' for k, v in [("villas","Villas"),("apartments","Apartments"),("hotel","Hotel"),("freehold","Freehold"),("ready","Ready now")])

page = f'''<title>Nuanu Bali Properties</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="Bali Invest: Nuanu Creative City projects in Bali with prices, photos, video tours and the Nuanu map. Ask Florin on WhatsApp {WA_DISPLAY}.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=Manrope:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Layout: full-bleed hero photo, then alternating project spreads (gallery | facts | phone video), dark CTA bands every few projects */
:root {{
  --bg: #ECEEE8; --surface: #F8F9F5; --ink: #13201A; --muted: #56645B; --line: #CDD4CA;
  --accent: #A8692A; --wa: #0F7A40; --wa-ink: #FFFFFF; --band: #12201A; --band-ink: #EEF1EA; --band-muted: #A9B8AD;
  --display: "Syne", "Avenir Next", "Segoe UI", sans-serif;
  --body: "Manrope", "Segoe UI", system-ui, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
  --r: 14px;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #0C130F; --surface: #131C17; --ink: #E7ECE5; --muted: #9AA89E; --line: #27342C;
  --accent: #D9A35E; --wa: #1FA85A; --wa-ink: #06130B; --band: #18271F; --band-ink: #EEF1EA; --band-muted: #A9B8AD; color-scheme: dark; }} }}
:root[data-theme="dark"] {{
  --bg: #0C130F; --surface: #131C17; --ink: #E7ECE5; --muted: #9AA89E; --line: #27342C;
  --accent: #D9A35E; --wa: #1FA85A; --wa-ink: #06130B; --band: #18271F; --band-ink: #EEF1EA; --band-muted: #A9B8AD; color-scheme: dark; }}
*, *::before, *::after {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; scroll-padding-top: calc(env(safe-area-inset-top, 0px) + 72px); }}
@media (prefers-reduced-motion: reduce) {{ html {{ scroll-behavior: auto; }} *, *::before, *::after {{ transition: none !important; animation: none !important; }} }}
body {{ background: var(--bg); color: var(--ink); font-family: var(--body); font-size: 16px; line-height: 1.6; -webkit-font-smoothing: antialiased; }}
body::before {{ content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10; background: var(--surface); }}
img {{ max-width: 100%; display: block; }}
a {{ color: inherit; }}
.mono {{ font-family: var(--mono); }}
.wrap {{ max-width: 1240px; margin: 0 auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}
h1, h2, h3 {{ font-family: var(--display); line-height: 1.04; letter-spacing: -0.01em; text-wrap: balance; margin: 0; }}
.eyebrow {{ font-family: var(--mono); font-size: 12px; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); margin: 0; }}
:focus-visible {{ outline: 3px solid var(--accent); outline-offset: 3px; border-radius: 6px; }}

/* top bar */
.bar {{ position: sticky; top: env(safe-area-inset-top, 0px); z-index: 20; background: color-mix(in srgb, var(--surface) 92%, transparent); backdrop-filter: blur(10px); border-bottom: 1px solid var(--line); }}
.bar .wrap {{ display: flex; align-items: center; justify-content: space-between; gap: 12px; padding-block: 10px; }}
.brand {{ display: flex; align-items: center; gap: 10px; text-decoration: none; }}
.brand .face {{ width: 40px; height: 40px; }}
.brand b {{ font-family: var(--display); font-size: 18px; letter-spacing: .02em; }}
.brand small {{ display: block; font-family: var(--mono); font-size: 11px; color: var(--muted); letter-spacing: .08em; }}
.bar nav {{ display: flex; gap: 18px; font-size: 14px; font-weight: 600; }}
.bar nav a {{ text-decoration: none; color: var(--muted); }}
.bar nav a:hover {{ color: var(--ink); }}
@media (max-width: 820px) {{ .bar nav {{ display: none; }} }}
@media (max-width: 480px) {{ .brand small {{ display: none; }} }}

.btn {{ display: inline-flex; align-items: center; gap: 10px; padding: 12px 18px; border-radius: 999px; font-weight: 700; font-size: 15px; text-decoration: none; border: 0; cursor: pointer; line-height: 1.2; }}
.btn.wa {{ background: var(--wa); color: var(--wa-ink); }}
.btn.wa:hover {{ filter: brightness(1.08); }}
.btn.ghost {{ background: transparent; color: inherit; border: 1.5px solid currentColor; }}
.btn.sm {{ padding: 9px 14px; font-size: 14px; }}
.ico {{ width: 20px; height: 20px; flex: none; }}
.face {{ border-radius: 50%; width: 52px; height: 52px; object-fit: cover; flex: none; }}

/* hero */
.hero {{ position: relative; color: #F4F6F1; background: #0d1511; }}
.hero picture img {{ width: 100%; height: min(78vh, 760px); min-height: 520px; object-fit: cover; }}
.hero::after {{ content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(8,14,10,.15) 0%, rgba(8,14,10,.05) 35%, rgba(8,14,10,.78) 100%); pointer-events: none; }}
.hero-copy {{ position: absolute; inset: auto 0 0 0; z-index: 2; padding-block: 0 44px; }}
.hero-copy .eyebrow {{ color: #E4EAE2; text-shadow: 0 1px 8px rgba(0,0,0,.6); }}
.hero p.lead, .coords {{ text-shadow: 0 1px 10px rgba(0,0,0,.55); }}
.hero h1 {{ font-size: clamp(44px, 9vw, 120px); font-weight: 800; margin: 10px 0 14px; letter-spacing: -0.02em; }}
.hero h1 em {{ font-style: normal; color: #E7B877; }}
.hero p.lead {{ max-width: 56ch; font-size: clamp(16px, 2vw, 19px); color: #E4EAE2; margin: 0 0 22px; }}
.hero-row {{ display: flex; flex-wrap: wrap; align-items: center; gap: 14px; }}
.hero .btn.ghost {{ color: #F4F6F1; }}
.coords {{ position: absolute; top: 18px; right: max(16px, env(safe-area-inset-right, 0px)); z-index: 2; font-family: var(--mono); font-size: 12px; color: #E4EAE2; letter-spacing: .08em; text-align: right; }}

/* about Nuanu + map */
.intro {{ padding-block: 72px 24px; }}
.intro-grid {{ display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.25fr); gap: 48px; align-items: start; }}
.intro h2 {{ font-size: clamp(32px, 4.4vw, 54px); margin-top: 10px; }}
.intro p {{ max-width: 62ch; color: var(--muted); }}
.stats {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px 24px; margin: 26px 0 0; padding: 0; }}
.stats div {{ border-top: 1px solid var(--line); padding-top: 10px; }}
.stats dt {{ font-family: var(--display); font-size: 30px; font-weight: 700; color: var(--ink); }}
.stats dd {{ margin: 0; color: var(--muted); font-size: 14px; }}
.map {{ margin: 0; background: var(--surface); border: 1px solid var(--line); border-radius: var(--r); overflow: hidden; }}
.map img {{ width: 100%; height: auto; cursor: zoom-in; }}
.map figcaption {{ display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap; padding: 12px 16px; font-size: 13px; color: var(--muted); }}
@media (max-width: 900px) {{ .intro-grid {{ grid-template-columns: minmax(0, 1fr); gap: 28px; }} }}

/* index */
.index {{ padding-block: 40px 24px; }}
.index-head {{ display: flex; justify-content: space-between; align-items: end; gap: 16px; flex-wrap: wrap; margin-bottom: 18px; }}
.index-head h2 {{ font-size: clamp(28px, 3.4vw, 40px); }}
.chips {{ display: flex; flex-wrap: wrap; gap: 8px; }}
.chip {{ font: 600 14px var(--body); padding: 8px 14px; border-radius: 999px; border: 1.5px solid var(--line); background: var(--surface); color: var(--ink); cursor: pointer; }}
.chip[aria-pressed="true"] {{ background: var(--ink); color: var(--bg); border-color: var(--ink); }}
.ix-grid {{ list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 14px; }}
.ix a {{ display: block; text-decoration: none; position: relative; border-radius: 12px; overflow: hidden; background: var(--surface); }}
.ix img {{ width: 100%; aspect-ratio: 4/3; object-fit: cover; transition: transform .5s ease; }}
.ix a:hover img {{ transform: scale(1.04); }}
.ix-meta {{ display: flex; flex-direction: column; padding: 10px 12px 12px; gap: 2px; }}
.ix-name {{ font-weight: 700; font-size: 15px; line-height: 1.25; }}
.ix-price {{ font-size: 12.5px; color: var(--accent); }}
.ix.dim {{ display: none; }}
.ix-beds {{ font-size: 12px; color: var(--muted); }}
.filters {{ display: grid; gap: 10px; margin-bottom: 20px; }}
.frow {{ display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }}
.flabel {{ font-size: 11.5px; letter-spacing: .1em; text-transform: uppercase; color: var(--muted); width: 6.5em; }}
.fstatus {{ margin: 0; font-size: 14px; color: var(--muted); min-height: 1.4em; }}
.fstatus button {{ font: 600 14px var(--body); background: none; border: 0; color: var(--accent); cursor: pointer; text-decoration: underline; padding: 0 4px; }}
.b-card.dim {{ display: none; }}
.thumbs li {{ position: relative; }}
.thumbs .more {{ position: absolute; inset: 0; display: grid; place-items: center; background: rgba(10,16,12,.55); color: #fff; font: 700 18px var(--display); border-radius: 10px; pointer-events: none; }}
@media (max-width: 1100px) {{ .ix-grid {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }} }}
@media (max-width: 600px) {{ .ix-grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }} }}

/* project spreads */
.project {{ padding-block: 64px; border-top: 1px solid var(--line); }}
.project.dim {{ display: none; }}
.p-head {{ display: grid; gap: 6px; margin-bottom: 24px; }}
.p-index {{ font-size: 12px; letter-spacing: .1em; color: var(--accent); margin: 0; }}
.p-head h2 {{ font-size: clamp(34px, 5vw, 64px); font-weight: 800; }}
.p-kind {{ margin: 0; color: var(--muted); font-weight: 500; }}
.tags {{ display: flex; flex-wrap: wrap; gap: 6px; margin-top: 4px; }}
.tag {{ font-family: var(--mono); font-size: 11.5px; letter-spacing: .06em; text-transform: uppercase; padding: 3px 9px; border: 1px solid var(--line); border-radius: 999px; color: var(--muted); }}
.p-grid {{ display: grid; grid-template-columns: minmax(0, 1.55fr) minmax(0, 1fr) 250px; gap: 32px; align-items: start; }}
.project:nth-of-type(even) .gallery {{ order: 2; }}
.project:nth-of-type(even) .p-info {{ order: 1; }}
.project:nth-of-type(even) .phone {{ order: 3; }}
.gallery {{ display: grid; gap: 10px; min-width: 0; }}
.g-main {{ width: 100%; aspect-ratio: 3/2; object-fit: cover; border-radius: var(--r); cursor: zoom-in; background: var(--line); }}
.thumbs {{ list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 10px; }}
.thumbs img {{ width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 10px; cursor: zoom-in; background: var(--line); }}
.thumbs.small {{ grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px; }}
.p-info {{ min-width: 0; }}
.price {{ font-family: var(--display); font-size: clamp(34px, 3.6vw, 46px); font-weight: 700; margin: 0 0 14px; color: var(--ink); font-variant-numeric: tabular-nums; }}
.price.sm {{ font-size: 30px; margin-bottom: 10px; }}
.price .from {{ font-size: 13px; font-weight: 400; letter-spacing: .1em; text-transform: uppercase; color: var(--accent); vertical-align: middle; margin-right: 4px; }}
.facts {{ margin: 0 0 16px; display: grid; gap: 0; }}
.fact {{ display: grid; grid-template-columns: 9.5em minmax(0, 1fr); gap: 10px; padding: 9px 0; border-bottom: 1px solid var(--line); font-size: 14.5px; }}
.fact dt {{ color: var(--muted); font-family: var(--mono); font-size: 12px; letter-spacing: .06em; text-transform: uppercase; padding-top: 3px; }}
.fact dd {{ margin: 0; font-weight: 600; }}
.fact sup {{ color: var(--accent); }}
.about {{ color: var(--muted); margin: 0 0 14px; }}
.amen {{ list-style: none; padding: 0; margin: 0 0 20px; display: flex; flex-wrap: wrap; gap: 6px; }}
.amen li {{ font-size: 13px; padding: 5px 10px; background: var(--surface); border: 1px solid var(--line); border-radius: 8px; }}
.ask {{ display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }}
.phone {{ margin: 0; display: grid; gap: 8px; justify-items: center; }}
.phone video {{ width: 100%; max-width: 250px; aspect-ratio: 9/16; border-radius: 22px; background: #000; border: 6px solid var(--ink); object-fit: cover; }}
.phone figcaption {{ font-size: 12px; color: var(--muted); letter-spacing: .06em; }}
@media (max-width: 1100px) {{
  .p-grid {{ grid-template-columns: minmax(0, 1.3fr) minmax(0, 1fr); }}
  .phone {{ grid-column: 1 / -1; }}
  .project:nth-of-type(even) .gallery, .project:nth-of-type(even) .p-info {{ order: 0; }}
}}
@media (max-width: 760px) {{
  .p-grid {{ grid-template-columns: minmax(0, 1fr); gap: 22px; }}
  .thumbs {{ grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 6px; }}
  .project {{ padding-block: 44px; }}
  .fact {{ grid-template-columns: 8em minmax(0, 1fr); }}
}}

/* CTA band */
.cta-band {{ background: var(--band); color: var(--band-ink); }}
.cta-inner {{ display: grid; grid-template-columns: auto minmax(0, 1fr) auto; gap: 28px; align-items: center; padding-block: 44px; }}
.cta-band .eyebrow {{ color: var(--band-muted); }}
.cta-band h3 {{ font-size: clamp(24px, 3vw, 36px); margin: 6px 0 8px; }}
.cta-sub {{ margin: 0; color: var(--band-muted); max-width: 54ch; }}
.face.big {{ width: 120px; height: 120px; }}
.cta-actions {{ display: grid; gap: 8px; justify-items: center; }}
.cta-actions .num {{ font-size: 14px; color: var(--band-muted); user-select: all; }}
.cta-band .btn.wa {{ background: #1FA85A; color: #06130B; }}
@media (max-width: 760px) {{ .cta-inner {{ grid-template-columns: minmax(0, 1fr); justify-items: start; gap: 18px; }} .cta-actions {{ justify-items: start; }} .face.big {{ width: 92px; height: 92px; }} }}

/* BREIG */
.breig {{ padding-block: 80px 40px; border-top: 1px solid var(--line); }}
.breig-head {{ display: grid; gap: 10px; margin-bottom: 28px; max-width: 70ch; }}
.breig-head h2 {{ font-size: clamp(32px, 4.4vw, 54px); }}
.breig-head p {{ margin: 0; color: var(--muted); }}
.b-grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 28px; }}
.b-card {{ background: var(--surface); border: 1px solid var(--line); border-radius: var(--r); overflow: hidden; display: grid; align-content: start; }}
.b-main {{ width: 100%; aspect-ratio: 16/10; object-fit: cover; cursor: zoom-in; }}
.b-card .thumbs.small {{ padding: 8px 8px 0; }}
.b-body {{ padding: 18px 20px 22px; display: grid; gap: 8px; }}
.b-body h3 {{ font-size: 30px; }}
.b-body .facts {{ margin-bottom: 6px; }}
@media (max-width: 860px) {{ .b-grid {{ grid-template-columns: minmax(0, 1fr); }} }}

/* contact */
.contact {{ padding-block: 80px; background: var(--surface); border-top: 1px solid var(--line); }}
.contact-grid {{ display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 40px; align-items: center; }}
.contact .face.xl {{ width: 220px; height: 220px; }}
.contact h2 {{ font-size: clamp(36px, 5vw, 64px); margin: 8px 0 14px; }}
.contact p {{ color: var(--muted); max-width: 58ch; }}
.lines {{ display: grid; gap: 10px; margin: 20px 0 24px; }}
.line {{ display: flex; flex-wrap: wrap; align-items: center; gap: 10px; font-size: 18px; }}
.line .k {{ font-family: var(--mono); font-size: 12px; letter-spacing: .1em; text-transform: uppercase; color: var(--muted); width: 7.5em; }}
.line .v {{ font-weight: 700; user-select: all; overflow-wrap: anywhere; }}
.copy {{ font: 600 12px var(--body); padding: 5px 10px; border-radius: 999px; border: 1px solid var(--line); background: var(--bg); color: var(--ink); cursor: pointer; }}
@media (max-width: 760px) {{ .contact-grid {{ grid-template-columns: minmax(0, 1fr); gap: 20px; }} .contact .face.xl {{ width: 140px; height: 140px; }} }}
.company {{ margin-top: 56px; padding-top: 32px; border-top: 1px solid var(--line); display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.6fr); gap: 40px; }}
.co-head h3 {{ font-size: clamp(24px, 3vw, 34px); margin: 8px 0 10px; }}
.co-head p {{ color: var(--muted); margin: 0; }}
.co-facts {{ margin: 0; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px 28px; }}
.co-facts div {{ border-top: 1px solid var(--line); padding-top: 8px; min-width: 0; }}
.co-facts dt {{ font-family: var(--mono); font-size: 11.5px; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); }}
.co-facts dd {{ margin: 2px 0 0; font-weight: 600; font-size: 15px; overflow-wrap: anywhere; }}
@media (max-width: 860px) {{ .company {{ grid-template-columns: minmax(0, 1fr); gap: 20px; }} .co-facts {{ grid-template-columns: minmax(0, 1fr); }} }}
.disclaimer {{ padding-block: 28px 110px; font-size: 12.5px; color: var(--muted); }}
.disclaimer p {{ max-width: 100ch; margin: 0 0 8px; }}

/* floating bubble */
.float {{ position: fixed; z-index: 30; right: calc(16px + env(safe-area-inset-right, 0px)); bottom: calc(16px + env(safe-area-inset-bottom, 0px)); display: flex; align-items: center; gap: 0; text-decoration: none; }}
.float .face {{ width: 68px; height: 68px; box-shadow: 0 8px 24px rgba(0,0,0,.28); }}
.float .badge {{ position: absolute; right: -2px; bottom: -2px; width: 28px; height: 28px; border-radius: 50%; background: #1FA85A; color: #fff; display: grid; place-items: center; border: 2px solid var(--surface); }}
.float .badge .ico {{ width: 16px; height: 16px; }}
.float .label {{ background: var(--surface); color: var(--ink); border: 1px solid var(--line); font-weight: 700; font-size: 14px; padding: 9px 14px; border-radius: 999px; margin-right: 10px; box-shadow: 0 6px 18px rgba(0,0,0,.14); white-space: nowrap; }}
@media (max-width: 520px) {{ .float .label {{ display: none; }} .float .face {{ width: 60px; height: 60px; }} }}

/* lightbox */
dialog.lb {{ border: 0; padding: 0; background: transparent; width: 100vw; height: 100vh; max-width: 100vw; max-height: 100vh; overflow: hidden; }}
dialog.lb::backdrop {{ background: rgba(5,9,7,.92); }}
.lb-stage {{ width: 100%; height: 100%; display: grid; place-items: center; touch-action: pan-y; }}
dialog.lb img {{ max-width: 94vw; max-height: 80vh; object-fit: contain; border-radius: 10px; user-select: none; -webkit-user-drag: none; transition: opacity .15s ease; }}
dialog.lb .lb-nav {{ position: fixed; top: 50%; transform: translateY(-50%); width: 52px; height: 52px; border-radius: 50%; border: 0; background: rgba(244,246,241,.92); color: #13201A; font: 700 28px/1 var(--body); cursor: pointer; display: grid; place-items: center; padding: 0 0 4px; }}
dialog.lb .lb-prev {{ left: calc(12px + env(safe-area-inset-left, 0px)); }}
dialog.lb .lb-next {{ right: calc(12px + env(safe-area-inset-right, 0px)); }}
dialog.lb .lb-count {{ position: fixed; bottom: calc(22px + env(safe-area-inset-bottom, 0px)); left: 50%; transform: translateX(-50%); color: #EEF1EA; font: 500 14px var(--mono); letter-spacing: .08em; }}
@media (max-width: 600px) {{ dialog.lb .lb-nav {{ width: 48px; height: 48px; top: auto; bottom: calc(10px + env(safe-area-inset-bottom, 0px)); transform: none; }} }}
dialog.lb #lb-close {{ position: fixed; top: calc(14px + env(safe-area-inset-top, 0px)); right: calc(14px + env(safe-area-inset-right, 0px)); font: 700 15px var(--body); padding: 10px 16px; border-radius: 999px; border: 0; background: #F4F6F1; color: #13201A; cursor: pointer; }}
</style>

<header class="bar">
  <div class="wrap">
    <a class="brand" href="#top"><img class="face" src="media/img/florin-s.webp" alt="" width="40" height="40"><span><b>BALI INVEST</b><small>Florin · Nuanu & Bali property</small></span></a>
    <nav aria-label="Sections"><a href="#nuanu">Nuanu</a><a href="#map">Map</a><a href="#projects">Projects</a><a href="#breig">BREIG villas</a><a href="#contact">Contact</a></nav>
    <a class="btn wa sm" href="{wa("Hello Florin, I'd like details about property in Nuanu, Bali.")}" target="_blank" rel="noopener">{WA_ICON}<span>WhatsApp</span></a>
  </div>
</header>

<section class="hero" id="top">
  <picture>
    <source media="(max-width: 700px)" srcset="media/img/luna-residences_2-s.webp 800w, media/img/luna-residences_2.webp 1600w">
    <img src="media/img/luna-residences_6.webp" srcset="media/img/luna-residences_6-s.webp 800w, media/img/luna-residences_6.webp 1600w" sizes="100vw" alt="Luna Residences on the black-sand coast of Nuanu, Bali" fetchpriority="high">
  </picture>
  <p class="coords" aria-hidden="true">8°38′S 115°06′E<br>Tabanan · West Bali</p>
  <div class="hero-copy"><div class="wrap">
    <p class="eyebrow">Bali Invest · Property presentation</p>
    <h1>Nuanu, <em>Bali.</em></h1>
    <p class="lead">Fifteen projects inside Nuanu Creative City on Bali's west coast, plus a selection of BREIG villas across the island. Prices, key facts, renders and video tours in one place.</p>
    <div class="hero-row">
      <a class="btn wa" href="{wa("Hello Florin, I saw your Nuanu projects page and I'd like more details.")}" target="_blank" rel="noopener">{WA_ICON}<span>Ask Florin on WhatsApp</span></a>
      <a class="btn ghost" href="#projects">See the projects</a>
    </div>
  </div></div>
</section>

<section class="intro" id="nuanu">
  <div class="wrap intro-grid">
    <div>
      <p class="eyebrow">About the area</p>
      <h2>A creative city on the black-sand coast</h2>
      <p>Nuanu is a master-planned creative city in Tabanan, on Bali's west coast, about 15 minutes from Canggu. It mixes villas, residences and hotels with beach clubs, art spaces, international schools, wellness and restaurants, all inside one walkable, landscaped community next to Nyanyi Beach.</p>
      <p>Every project on this page sits inside Nuanu and uses its shared infrastructure. Several offer freehold ownership for foreign buyers.</p>
      <dl class="stats">
        <div><dt>44 ha</dt><dd>of planned city infrastructure</dd></div>
        <div><dt>15</dt><dd>projects in this presentation</dd></div>
        <div><dt>$115k</dt><dd>lowest starting price (Black Sands Oasis)</dd></div>
        <div><dt>~15 min</dt><dd>drive to Canggu</dd></div>
      </dl>
    </div>
    <figure class="map" id="map">
      <img src="media/img/nuanu-map-s.webp" srcset="media/img/nuanu-map-s.webp 1200w, media/img/nuanu-map.webp 2400w" sizes="(min-width: 900px) 55vw, 100vw" alt="Map of Nuanu Creative City with project locations" loading="lazy" data-zoom="media/img/nuanu-map.webp" width="1200" height="901">
      <figcaption><span>Nuanu Creative City masterplan. Tap to enlarge.</span><a href="{wa("Hello Florin, can you send me the Nuanu map with the project locations?")}" target="_blank" rel="noopener">Ask for the full map</a></figcaption>
    </figure>
  </div>
</section>

<section class="index" id="projects" aria-label="Project index">
  <div class="wrap">
    <div class="index-head">
      <h2>All Nuanu projects</h2>
    </div>
    <div class="filters">
      <div class="frow"><span class="flabel mono">Type</span><div class="chips" role="group" aria-label="Filter by type">{filters}</div></div>
      <div class="frow"><span class="flabel mono">Bedrooms</span><div class="chips" role="group" aria-label="Filter by bedrooms">{bed_filters}</div></div>
      <p class="fstatus" id="fstatus" aria-live="polite"></p>
    </div>
    <ul class="ix-grid">{"".join(index_card(p, i) for i, p in enumerate(NUANU, 1))}</ul>
  </div>
</section>

{"".join(sections)}

<section class="breig" id="breig">
  <div class="wrap">
    <div class="breig-head">
      <p class="eyebrow">Beyond Nuanu · BREIG Property</p>
      <h2>BREIG villas across Bali</h2>
      <p>BREIG Property is a Bali developer founded in 2016, with completed projects in Canggu, Pererenan, Ubud and Nusa Dua and its own management and construction companies. A selection of their villas for sale:</p>
    </div>
    <div class="b-grid">{"".join(breig_card(b) for b in BREIG)}</div>
  </div>
</section>

{cta_band("Not sure where to start? Tell me your budget and I'll shortlist.", "Hello Florin, my budget is ... and I'm looking for ... in Bali. Can you shortlist some options?", 99)}

<section class="contact" id="contact">
  <div class="wrap contact-grid">
    <img class="face xl" src="media/img/florin.webp" alt="Florin, Bali Invest" width="220" height="220" loading="lazy">
    <div>
      <p class="eyebrow">Talk to Florin</p>
      <h2>Bali Invest</h2>
      <p>I help investors from Europe and Australia buy property in Bali, from the first shortlist to the notary. Message me for brochures, layouts, payment plans and video calls.</p>
      <div class="lines">
        <div class="line"><span class="k">WhatsApp</span><span class="v mono" id="v-wa">{WA_DISPLAY}</span><button class="copy" type="button" data-copy="{WA_DISPLAY}" id="c-wa">Copy</button></div>
        <div class="line"><span class="k">Email</span><span class="v mono" id="v-em">{EMAIL}</span><button class="copy" type="button" data-copy="{EMAIL}" id="c-em">Copy</button></div>
      </div>
      <a class="btn wa" href="{wa("Hello Florin, I'd like details about property in Bali.")}" target="_blank" rel="noopener">{WA_ICON}<span>Message on WhatsApp</span></a>
    </div>
  </div>
  <div class="wrap">
    <div class="company">
      <div class="co-head">
        <p class="eyebrow">Registered company in Bali</p>
        <h3>PT Bali Investment Experts</h3>
        <p>Foreign-owned Indonesian company (PT PMA), registered with the Ministry of Law of the Republic of Indonesia (AHU). Bali Invest is its property brand.</p>
      </div>
      <dl class="co-facts">
        <div><dt>Director</dt><dd>Florin Dragu</dd></div>
        <div><dt>Company type</dt><dd>PT PMA (foreign investment)</dd></div>
        <div><dt>Deed of establishment</dt><dd>No. 01, 2 August 2025, notary Komang Rio Anjana S.H., M.Kn.</dd></div>
        <div><dt>Licensed activities</dt><dd>Real estate agency &amp; brokerage (KBLI 68200), real estate (KBLI 68111), investment &amp; management consulting (KBLI 70209)</dd></div>
        <div><dt>Registered office</dt><dd>Jalan Pengubungan, Gang Kayu Damar, Kerobokan, Kuta Utara, Badung, Bali, Indonesia</dd></div>
      </dl>
    </div>
  </div>
</section>

<footer class="disclaimer"><div class="wrap">
  <p><sup>*</sup>Projected yields are developer estimates and are not guaranteed. Prices are starting prices in USD and may change; please confirm current prices before any decision. Visuals are developer renders and photos.</p>
  <p>Nuanu project data: Nuanu Real Estate partner portal. BREIG data: public listings (Rumavi, Realting, Lazudi), indicative only. © Bali Invest · PT Bali Investment Experts (PT PMA), Kerobokan, Badung, Bali · Florin Dragu, Director · {WA_DISPLAY} · {EMAIL}</p>
</div></footer>

<a class="float" href="{wa("Hello Florin, I'd like details about property in Bali.")}" target="_blank" rel="noopener" aria-label="Chat with Florin on WhatsApp">
  <span class="label">Ask Florin for details</span>
  <img class="face" src="media/img/florin-s.webp" srcset="media/img/florin-s.webp 1x, media/img/florin.webp 2x" alt="" width="68" height="68">
  <span class="badge">{WA_ICON}</span>
</a>

<dialog class="lb" id="lb" aria-label="Photo viewer"><div class="lb-stage" id="lb-stage"><img id="lb-img" alt=""></div><button type="button" class="lb-nav lb-prev" id="lb-prev" aria-label="Previous photo">&#8249;</button><button type="button" class="lb-nav lb-next" id="lb-next" aria-label="Next photo">&#8250;</button><span class="lb-count" id="lb-count"></span><button type="button" id="lb-close">Close</button></dialog>

<script>
(function () {{
  var lb = document.getElementById('lb'), lbImg = document.getElementById('lb-img'), lbCount = document.getElementById('lb-count');
  var prevBtn = document.getElementById('lb-prev'), nextBtn = document.getElementById('lb-next');
  var set = [], pos = 0;
  function show(i) {{
    if (!set.length) return;
    pos = (i + set.length) % set.length;
    var el = set[pos];
    lbImg.src = el.getAttribute('data-zoom');
    lbImg.alt = el.getAttribute('alt') || el.getAttribute('data-alt') || '';
    lbCount.textContent = set.length > 1 ? (pos + 1) + ' / ' + set.length : '';
    prevBtn.hidden = nextBtn.hidden = set.length < 2;
    var nx = set[(pos + 1) % set.length]; if (nx) {{ var pre = new Image(); pre.src = nx.getAttribute('data-zoom'); }}
  }}
  function open(el) {{
    var g = el.getAttribute('data-gal');
    set = g ? Array.prototype.slice.call(document.querySelectorAll('[data-gal="' + g + '"]')).sort(function (a, b) {{ return a.dataset.idx - b.dataset.idx; }}) : [el];
    show(g ? set.indexOf(el) : 0);
    if (lb.showModal && !lb.open) lb.showModal();
  }}
  document.addEventListener('click', function (ev) {{
    var t = ev.target.closest('[data-zoom]');
    if (t) open(t);
  }});
  prevBtn.addEventListener('click', function (ev) {{ ev.stopPropagation(); show(pos - 1); }});
  nextBtn.addEventListener('click', function (ev) {{ ev.stopPropagation(); show(pos + 1); }});
  document.getElementById('lb-close').addEventListener('click', function () {{ lb.close(); }});
  document.getElementById('lb-stage').addEventListener('click', function (ev) {{ if (ev.target.id === 'lb-stage') lb.close(); }});
  document.addEventListener('keydown', function (ev) {{
    if (!lb.open) return;
    if (ev.key === 'ArrowRight') {{ show(pos + 1); ev.preventDefault(); }}
    else if (ev.key === 'ArrowLeft') {{ show(pos - 1); ev.preventDefault(); }}
  }});
  var sx = null, sy = 0;
  lb.addEventListener('touchstart', function (ev) {{ if (ev.touches.length === 1) {{ sx = ev.touches[0].clientX; sy = ev.touches[0].clientY; }} }}, {{ passive: true }});
  lb.addEventListener('touchend', function (ev) {{
    if (sx === null) return;
    var dx = ev.changedTouches[0].clientX - sx, dy = ev.changedTouches[0].clientY - sy; sx = null;
    if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) show(dx < 0 ? pos + 1 : pos - 1);
  }}, {{ passive: true }});

  var fType = null, fBed = null, status = document.getElementById('fstatus');
  function applyFilters() {{
    document.querySelectorAll('.chip[data-f]').forEach(function (o) {{ o.setAttribute('aria-pressed', o.dataset.f === fType ? 'true' : 'false'); }});
    document.querySelectorAll('.chip[data-b]').forEach(function (o) {{ o.setAttribute('aria-pressed', o.dataset.b === fBed ? 'true' : 'false'); }});
    var n = 0, nb = 0;
    document.querySelectorAll('.ix, .project, .b-card').forEach(function (el) {{
      var okT = !fType || el.dataset.tags.split(' ').indexOf(fType) > -1;
      var okB = !fBed || el.dataset.beds.split(' ').indexOf(fBed) > -1;
      var on = okT && okB;
      el.classList.toggle('dim', !on);
      if (on && el.classList.contains('ix')) n++;
      if (on && el.classList.contains('b-card')) nb++;
    }});
    if (!fType && !fBed) {{ status.textContent = ''; return; }}
    status.innerHTML = '';
    status.appendChild(document.createTextNode(n + ' Nuanu project' + (n === 1 ? '' : 's') + ' and ' + nb + ' BREIG villa project' + (nb === 1 ? '' : 's') + ' match.'));
    var clr = document.createElement('button'); clr.type = 'button'; clr.textContent = 'Clear filters';
    clr.addEventListener('click', function () {{ fType = null; fBed = null; applyFilters(); }});
    status.appendChild(clr);
  }}
  document.querySelectorAll('.chip[data-f]').forEach(function (c) {{
    c.addEventListener('click', function () {{ fType = (fType === c.dataset.f) ? null : c.dataset.f; applyFilters(); }});
  }});
  document.querySelectorAll('.chip[data-b]').forEach(function (c) {{
    c.addEventListener('click', function () {{ fBed = (fBed === c.dataset.b) ? null : c.dataset.b; applyFilters(); }});
  }});

  document.querySelectorAll('.copy').forEach(function (b) {{
    b.addEventListener('click', function () {{
      var txt = b.dataset.copy;
      var done = function () {{ b.textContent = 'Copied'; setTimeout(function () {{ b.textContent = 'Copy'; }}, 1600); }};
      var fallback = function () {{ var r = document.createRange(); r.selectNodeContents(b.previousElementSibling); var s = getSelection(); s.removeAllRanges(); s.addRange(r); }};
      try {{ navigator.clipboard.writeText(txt).then(done, fallback); }} catch (e) {{ fallback(); }}
    }});
  }});

  // pause other videos when one plays
  document.querySelectorAll('video').forEach(function (v) {{
    v.addEventListener('play', function () {{ document.querySelectorAll('video').forEach(function (o) {{ if (o !== v) o.pause(); }}); }});
  }});
}})();
</script>
'''

os.makedirs("site", exist_ok=True)
open("site/index.html", "w").write(page)

# list used media
import re
used = sorted(set(re.findall(r'media/(?:img|v)/[\w.-]+', page)))
open("site/used.txt", "w").write("\n".join(used))
print(len(page), "bytes;", len(used), "media refs")
