"""
Created on Wed Sep 11 14:22:27 2024

@author: giftwarieta
"""

import streamlit as st
import pandas as pd
import mysql.connector
import os
from pathlib import Path
import base64
import textwrap
from dotenv import load_dotenv
import requests

# configuring time
from datetime import datetime
from datetime import date
from datetime import timedelta

today = date.today()
thisday = today.strftime('%A, %B %d %Y')

st.write('This script ran today, ' + thisday)

current_dir = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
env_path = current_dir / ".env"
load_dotenv(dotenv_path=env_path)

# Example of accessing an environment variable (change 'host' to your variable name)
host = os.getenv('HOST')
if host:
    st.write(f"Host: {host}")
else:
    st.write("Host environment variable not found")

# Access the secret from the environment variable
#APP_PASSWORD = os.getenv('APP_PASSWORD')
APP_PASSWORD = os.getenv('app_password')

auth_header = base64.b64encode(f"{APP_PASSWORD}".encode("ascii"))

# Display the secret (if found)
if APP_PASSWORD:
    st.write(f"The secret password is: {APP_PASSWORD}")
else:
    st.write("No password found")

st.write(auth_header)

# Access the secret from the environment variable
#password = os.getenv('APP_PASSWORD')
#APP_PASSWORD = os.getenv('app_password')

#st.write(APP_PASSWORD)
# Use the secret (password)
#if APP_PASSWORD:
 #   st.write(f"The secret password is: {APP_PASSWORD}")
#else:
 #   st.write("No password found")

#host = 'gewideas.com.ng'

#st.write(host)

data_df = pd.DataFrame(
    {
        "apps": [
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "apps": st.column_config.ImageColumn(
            "Preview Image", help="Streamlit app preview screenshots"
        )
    },
    hide_index=True,
)


def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)

def render_svg_example():
    svg = """
        <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
            <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
        </svg>
    """
    st.write('## Rendering an SVG in Streamlit')

    st.write('### SVG Input')
    st.code(textwrap.dedent(svg), 'svg')

    st.write('### SVG Output')
    render_svg(svg)

title = st.text_input("Movie title", "")

card_width = "200"
card_height = "100"

def mastercard_image():
    mastercard = st.markdown(
    f"""
    <svg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg' width='{card_width}' height='{card_height}' fill='#000000'><g id='SVGRepo_bgCarrier' stroke-width='0'></g><g id='SVGRepo_tracerCarrier' stroke-linecap='round' stroke-linejoin='round'></g><g id='SVGRepo_iconCarrier'> <g fill='none' fill-rule='evenodd'> <circle cx='7' cy='12' r='7' fill='#EA001B'></circle> <circle cx='17' cy='12' r='7' fill='#FFA200' fill-opacity='.8'></circle> </g> </g></svg>
    """
    , unsafe_allow_html=True)
    
def visacard_image():
    visacard = st.markdown(
        f"""
        <svg xmlns='http://www.w3.org/2000/svg' width='{card_width}' height='{card_height}' viewBox='0 0 256 83'><defs><linearGradient id='logosVisa0' x1='45.974%' x2='54.877%' y1='-2.006%' y2='100%'><stop offset='0%' stop-color='#222357'/><stop offset='100%' stop-color='#254aa5'/></linearGradient></defs><path fill='url(#logosVisa0)' d='M132.397 56.24c-.146-11.516 10.263-17.942 18.104-21.763c8.056-3.92 10.762-6.434 10.73-9.94c-.06-5.365-6.426-7.733-12.383-7.825c-10.393-.161-16.436 2.806-21.24 5.05l-3.744-17.519c4.82-2.221 13.745-4.158 23-4.243c21.725 0 35.938 10.724 36.015 27.351c.085 21.102-29.188 22.27-28.988 31.702c.069 2.86 2.798 5.912 8.778 6.688c2.96.392 11.131.692 20.395-3.574l3.636 16.95c-4.982 1.814-11.385 3.551-19.357 3.551c-20.448 0-34.83-10.87-34.946-26.428m89.241 24.968c-3.967 0-7.31-2.314-8.802-5.865L181.803 1.245h21.709l4.32 11.939h26.528l2.506-11.939H256l-16.697 79.963zm3.037-21.601l6.265-30.027h-17.158zm-118.599 21.6L88.964 1.246h20.687l17.104 79.963zm-30.603 0L53.941 26.782l-8.71 46.277c-1.022 5.166-5.058 8.149-9.54 8.149H.493L0 78.886c7.226-1.568 15.436-4.097 20.41-6.803c3.044-1.653 3.912-3.098 4.912-7.026L41.819 1.245H63.68l33.516 79.963z' transform='matrix(1 0 0 -1 0 82.668)'/></svg>
        """
        , unsafe_allow_html=True)

def discovercard_image():
    discover = st.markdown(
        f"""
        <svg xmlns='http://www.w3.org/2000/svg' width='{card_width}' height='{card_height}' viewBox='0 0 512 86'><defs><linearGradient id='logosDiscover0' x1='19.414%' x2='88.601%' y1='9.063%' y2='80.499%'><stop offset='0%' stop-color='#f34f26'/><stop offset='100%' stop-color='#f69e35'/></linearGradient><filter id='logosDiscover1' width='200%' height='200%' x='-50%' y='-50%' filterUnits='objectBoundingBox'><feMorphology in='SourceAlpha' radius='1' result='shadowSpreadInner1'/><feGaussianBlur in='shadowSpreadInner1' result='shadowBlurInner1' stdDeviation='4'/><feOffset dx='3' dy='3' in='shadowBlurInner1' result='shadowOffsetInner1'/><feComposite in='shadowOffsetInner1' in2='SourceAlpha' k2='-1' k3='1' operator='arithmetic' result='shadowInnerInner1'/><feColorMatrix in='shadowInnerInner1' values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.5 0'/></filter><path id='logosDiscover2' d='M270.356.365c-23.982 0-43.44 18.735-43.44 41.857c0 24.584 18.613 42.96 43.44 42.96c24.208 0 43.322-18.62 43.322-42.477c0-23.716-18.986-42.34-43.322-42.34'/></defs><use fill='url(#logosDiscover0)' fill-rule='evenodd' href='#logosDiscover2'/><use filter='url(#logosDiscover1)' href='#logosDiscover2'/><path fill='#0b1015' d='M23.746 1.891H.393v81.454h23.231c12.326 0 21.24-2.92 29.06-9.398c9.278-7.695 14.78-19.298 14.78-31.29c0-24.048-17.965-40.766-43.718-40.766m18.572 61.177c-5.021 4.53-11.486 6.488-21.76 6.488H16.29V15.684h4.268c10.274 0 16.491 1.834 21.76 6.592c5.495 4.886 8.772 12.452 8.772 20.265c0 7.83-3.277 15.66-8.772 20.527m32.48 20.277H90.67V1.891H74.8zm54.728-50.209c-9.539-3.534-12.346-5.865-12.346-10.246c0-5.134 4.998-9.039 11.849-9.039c4.763 0 8.671 1.953 12.836 6.58l8.295-10.853C143.32 3.581 135.139.532 126.214.532c-14.398 0-25.399 10.02-25.399 23.32c0 11.246 5.126 16.981 20.032 22.369c6.232 2.187 9.4 3.646 10.992 4.643c3.175 2.077 4.77 4.998 4.77 8.415c0 6.606-5.257 11.484-12.351 11.484c-7.574 0-13.674-3.782-17.34-10.865L96.67 69.802c7.314 10.733 16.11 15.512 28.214 15.512c16.488 0 28.084-11.007 28.084-26.758c0-12.949-5.36-18.816-23.442-25.42m28.448 9.522c0 23.965 18.816 42.525 43.006 42.525c6.839 0 12.701-1.352 19.915-4.759V61.727c-6.36 6.358-11.98 8.916-19.19 8.916c-15.996 0-27.363-11.606-27.363-28.102c0-15.626 11.722-27.964 26.638-27.964c7.561 0 13.311 2.685 19.915 9.158V5.04C213.933 1.51 208.183.054 201.343.054c-24.067 0-43.369 18.935-43.369 42.604m191.652 13.948L327.883 1.891h-17.346l34.58 83.535h8.543L388.843 1.89h-17.217zm46.44 26.74h45.065v-13.79h-29.189V47.555h28.072V33.763h-28.072v-18.08h29.189V1.892h-45.066zM504.02 25.93c0-15.259-10.49-24.039-28.823-24.039H451.62v81.454h15.895V50.608h2.08l21.975 32.737h19.544l-25.667-34.31c11.988-2.452 18.573-10.639 18.573-23.105m-31.882 13.452h-4.623V14.7h4.877c9.915 0 15.287 4.165 15.287 12.092c0 8.177-5.372 12.59-15.541 12.59'/></svg>
        """
        , unsafe_allow_html=True)


def americanexpresscard_image():
    americanexpress = st.markdown(
        f"""
        <svg xmlns='http://www.w3.org/2000/svg' width='{card_width}' height='{card_height}' viewBox='0 0 24 24'><path fill='#016FD0' d='M16.015 14.378c0-.32-.135-.496-.344-.622c-.21-.12-.464-.135-.81-.135h-1.543v2.82h.675v-1.027h.72c.24 0 .39.024.478.125c.12.13.104.38.104.55v.35h.66v-.555c-.002-.25-.017-.376-.108-.516a.75.75 0 0 0-.33-.234l.02-.008a.78.78 0 0 0 .48-.747zm-.87.407l-.028-.002c-.09.053-.195.058-.33.058h-.81v-.63h.824c.12 0 .24 0 .33.05a.27.27 0 0 1 .15.255c0 .12-.045.215-.134.27zm5.152 1.052H19v.6h1.304c.676 0 1.05-.278 1.05-.884c0-.28-.066-.448-.187-.582c-.153-.133-.392-.193-.73-.207l-.376-.015c-.104 0-.18 0-.255-.03a.21.21 0 0 1-.15-.21c0-.09.017-.166.09-.21a.5.5 0 0 1 .272-.06h1.23v-.602h-1.35c-.704 0-.958.437-.958.84c0 .9.776.855 1.407.87c.104 0 .18.015.225.06c.046.03.082.106.082.18c0 .077-.035.15-.08.18c-.06.053-.15.07-.277.07M0 0v10.096L.81 8.22h1.75l.225.464V8.22h2.043l.45 1.02l.437-1.013h6.502c.295 0 .56.057.756.236v-.23h1.787v.23c.307-.17.686-.23 1.12-.23h2.606l.24.466v-.466h1.918l.254.465v-.466h1.858v3.948H20.87l-.36-.6v.585h-2.353l-.256-.63h-.583l-.27.614h-1.213c-.48 0-.84-.104-1.08-.24v.24h-2.89v-.884c0-.12-.03-.12-.105-.135h-.105v1.036H6.067v-.48l-.21.48H4.69l-.202-.48v.465H2.235l-.256-.624H1.4l-.256.624H0V24h23.786v-7.108c-.27.135-.613.18-.973.18H21.09v-.255c-.21.165-.57.255-.914.255H14.71v-.9c0-.12-.018-.12-.12-.12h-.075v1.022h-1.8v-1.066c-.298.136-.643.15-.928.136h-.214v.915h-2.18l-.54-.617l-.57.6H4.742v-3.93h3.61l.518.602l.554-.6h2.412c.28 0 .74.03.942.225v-.24h2.177c.202 0 .644.045.903.225v-.24h3.265v.24c.163-.164.508-.24.803-.24h1.89v.24c.194-.15.464-.24.84-.24h1.176V0zm21.156 14.955l.01.016c.01.01.024.01.032.02zm2.672-1.873h.065v.555h-.065zm.037 1.948v-.005c-.03-.025-.046-.048-.075-.07c-.15-.153-.39-.215-.764-.225l-.36-.012a.9.9 0 0 1-.27-.03a.21.21 0 0 1-.15-.21q0-.136.09-.204c.076-.045.15-.05.27-.05h1.223v-.588h-1.283c-.69 0-.96.437-.96.84c0 .9.78.855 1.41.87c.104 0 .18.015.224.06c.046.03.076.106.076.18c0 .07-.034.138-.09.18c-.045.056-.136.07-.27.07h-1.288v.605h1.287c.42 0 .734-.118.9-.36h.03c.09-.134.135-.3.135-.523c0-.24-.045-.39-.135-.526zm-5.268-.822v-.583h-2.235v2.833h2.235v-.585h-1.57v-.57h1.533v-.584h-1.532v-.51M13.51 8.787h.685V11.6h-.684zm-.384.756l-.007.006c0-.314-.13-.5-.34-.624c-.217-.125-.47-.135-.81-.135H10.43v2.82h.674v-1.034h.72c.24 0 .39.03.487.12c.122.136.107.378.107.548v.354h.677v-.553c0-.25-.016-.375-.11-.516a.8.8 0 0 0-.33-.237c.172-.07.472-.3.472-.75zm-.855.396h-.015c-.09.054-.195.056-.33.056H11.1v-.623h.825c.12 0 .24.004.33.05c.09.04.15.128.15.25s-.047.22-.134.266zm3.649-.566h.632v-.6h-.644c-.464 0-.804.105-1.02.33c-.286.3-.362.69-.362 1.11c0 .512.123.833.36 1.074c.232.238.645.31.97.31h.78l.255-.627h1.39l.262.627h1.36v-2.11l1.272 2.11h.95l.002.002V8.786h-.684v1.963l-1.18-1.96h-1.02V11.4L18.11 8.744h-1.004l-.943 2.22h-.3c-.177 0-.362-.03-.468-.134c-.125-.15-.186-.36-.186-.662c0-.285.08-.51.194-.63c.133-.135.272-.165.516-.165zm1.668-.108l.464 1.118v.002h-.93zM2.38 10.97l.254.628H4V9.393l.972 2.205h.584l.973-2.202l.015 2.202h.69v-2.81H6.118l-.807 1.904l-.876-1.905H3.343v2.663L2.205 8.787h-.997L.01 11.597h.72l.26-.626zm-.688-1.705l.46 1.118l-.003.002h-.915l.457-1.12zm10.164 4.355H9.714l-.85.923l-.825-.922H5.346v2.82H8l.855-.932l.824.93h1.302v-.94h.838c.6 0 1.17-.164 1.17-.945l-.006-.003c0-.78-.598-.93-1.128-.93zM7.67 15.853l-.014-.002H6.02v-.557h1.47v-.574H6.02v-.51H7.7l.733.82l-.764.824zm2.642.33l-1.03-1.147l1.03-1.108v2.253zm1.553-1.258h-.885v-.717h.885c.24 0 .42.098.42.344c0 .243-.15.372-.42.372zM9.967 9.373v-.586H7.73V11.6h2.237v-.58H8.4v-.564h1.527V9.88H8.4v-.507'/></svg>
        """
        , unsafe_allow_html=True)

def vervecard_image():
    verve = st.markdown(
        f"""
        <svg viewBox='0 -139.5 750 750' version='1.1' xmlns='http://www.w3.org/2000/svg'  width='{card_width}' height='{card_height}' xmlns:xlink='http://www.w3.org/1999/xlink' fill='#000000'><g id='SVGRepo_bgCarrier' stroke-width='0'></g><g id='SVGRepo_tracerCarrier' stroke-linecap='round' stroke-linejoin='round'></g><g id='SVGRepo_iconCarrier'> <desc>Created with Sketch.</desc> <defs> </defs> <g id='Page-1' stroke='none' stroke-width='1' fill='none' fill-rule='evenodd'> <g id='verve' fill-rule='nonzero'> <rect id='Rectangle-path' fill='#00425F' x='0' y='0' width='750' height='471' rx='40'> </rect> <circle id='Oval' fill='#EE312A' cx='156.26347' cy='215.5' r='115.26347'> </circle> <path d='M156.26347,264.87251 C130.48369,206.43174 111.57857,151.84021 111.57857,151.84021 L72.05384,151.84021 C72.05384,151.84021 96.11071,221.91184 140.79561,309.54065 L171.73134,309.54065 C216.41624,221.91184 240.47311,151.84021 240.47311,151.84021 L200.94837,151.84021 C200.94837,151.84021 182.04325,206.43174 156.26347,264.87251 Z' id='Shape' fill='#FFFFFF'> </path> <path d='M708.04515,257.60566 L630.71641,257.60566 C630.71641,257.60566 632.43441,283.3869 666.80307,283.3869 C683.98685,283.3869 701.17192,278.22677 701.17192,278.22677 L704.60925,305.72097 C704.60925,305.72097 687.42418,312.59491 663.36588,312.59491 C628.99845,312.59491 598.06688,295.41041 598.06688,247.29525 C598.06688,209.48978 622.12375,185.4322 656.4926,185.4322 C708.04515,185.4322 711.48248,236.98469 708.04515,257.60566 Z M654.77471,209.48978 C632.43436,209.48978 630.71641,233.54736 630.71641,233.54736 L678.83158,233.54736 C678.83158,233.54736 677.11363,209.48978 654.77471,209.48978 Z' id='Shape' fill='#FFFFFF'> </path> <path d='M442.3337,216.74823 L447.48884,189.25332 C447.48884,189.25332 407.67636,177.17202 375.31538,199.56388 L375.31538,309.54067 L409.68552,309.54067 L409.68281,220.18485 C423.42925,209.87443 442.3337,216.74823 442.3337,216.74823 Z' id='Shape' fill='#FFFFFF'> </path> <path d='M348.41613,257.60566 L271.08739,257.60566 C271.08739,257.60566 272.80539,283.3869 307.17405,283.3869 C324.35783,283.3869 341.54148,278.22677 341.54148,278.22677 L344.97881,305.72097 C344.97881,305.72097 327.79517,312.59491 303.73687,312.59491 C269.36802,312.59491 238.43649,295.41041 238.43649,247.29525 C238.43649,209.48978 262.49479,185.4322 296.86364,185.4322 C348.41613,185.4322 351.852,236.98469 348.41613,257.60566 Z M295.14426,209.48978 C272.80534,209.48978 271.08739,233.54736 271.08739,233.54736 L319.20256,233.54736 C319.20256,233.54736 317.4846,209.48978 295.14426,209.48978 Z' id='Shape' fill='#FFFFFF'> </path> <path d='M525.80355,268.32373 C515.12048,242.341853 506.501709,215.55843 500.02729,188.22223 L465.66129,188.22677 C465.66129,188.22677 482.845,254.57171 512.05993,309.5462 L539.54717,309.5462 C568.76212,254.57171 585.94581,188.239 585.94581,188.239 L551.57981,188.239 C545.103957,215.569341 536.48521,242.34708 525.80355,268.32373 Z' id='Shape' fill='#FFFFFF'> </path> </g> </g> </g></svg>
        """
        , unsafe_allow_html=True)

def maestrocard_image():
    maestro = st.markdown(
        f"""
        <svg xmlns='http://www.w3.org/2000/svg' width='{card_width}' height='{card_height}' viewBox='0 0 256 199'><path fill='#6c6bbd' d='M162.611 141.315H93.389V16.913h69.222z'/><path fill='#d32011' d='M97.783 79.117c0-25.236 11.815-47.715 30.215-62.201C114.543 6.323 97.56 0 79.106 0C35.416 0 0 35.421 0 79.117c0 43.695 35.416 79.116 79.106 79.116c18.455 0 35.437-6.323 48.892-16.916c-18.4-14.486-30.215-36.965-30.215-62.2'/><path fill='#0099df' d='M256 79.117c0 43.695-35.416 79.116-79.106 79.116c-18.455 0-35.437-6.323-48.897-16.916c18.405-14.486 30.22-36.965 30.22-62.2c0-25.236-11.815-47.715-30.22-62.201C141.457 6.323 158.44 0 176.894 0C220.584 0 256 35.421 256 79.117'/><path fill='#110f0d' d='M186.033 176.466c.92 0 2.243.176 3.254.573l-1.408 4.306c-.966-.397-1.932-.528-2.857-.528c-2.988 0-4.482 1.931-4.482 5.402v11.78h-4.572v-21.005h4.527v2.55c1.187-1.846 2.902-3.078 5.538-3.078m-16.891 4.703h-7.47v9.491c0 2.108.745 3.516 3.034 3.516c1.187 0 2.68-.397 4.039-1.187l1.317 3.909c-1.448 1.01-3.732 1.63-5.709 1.63c-5.407 0-7.293-2.903-7.293-7.782v-9.577h-4.265v-4.175h4.265v-6.373h4.612v6.373h7.47zm-58.494 4.482c.488-3.033 2.33-5.1 5.584-5.1c2.942 0 4.833 1.845 5.316 5.1zm15.649 1.846c-.046-6.55-4.09-11.031-9.98-11.031c-6.151 0-10.457 4.482-10.457 11.03c0 6.675 4.482 11.026 10.769 11.026c3.164 0 6.061-.79 8.611-2.942l-2.243-3.385c-1.755 1.408-3.999 2.198-6.106 2.198c-2.943 0-5.624-1.363-6.283-5.14h15.598c.045-.574.09-1.143.09-1.756m20.08-5.141c-1.273-.795-3.864-1.806-6.545-1.806c-2.505 0-3.999.926-3.999 2.465c0 1.403 1.58 1.8 3.557 2.062l2.153.307c4.572.664 7.338 2.596 7.338 6.288c0 3.998-3.516 6.855-9.577 6.855c-3.43 0-6.594-.88-9.1-2.726l2.154-3.561c1.539 1.187 3.828 2.198 6.991 2.198c3.119 0 4.789-.92 4.789-2.55c0-1.182-1.187-1.846-3.692-2.193l-2.153-.307c-4.703-.664-7.253-2.772-7.253-6.197c0-4.175 3.43-6.725 8.747-6.725c3.34 0 6.373.75 8.566 2.198zm56.36-1.55c-.94 0-1.81.167-2.62.494a6.3 6.3 0 0 0-2.093 1.388a6.4 6.4 0 0 0-1.388 2.138q-.504 1.246-.503 2.741c0 1.001.166 1.911.503 2.741q.506 1.247 1.388 2.138a6.3 6.3 0 0 0 2.093 1.388c.81.332 1.68.493 2.62.493s1.816-.16 2.62-.493a6.3 6.3 0 0 0 2.103-1.388c.599-.593 1.062-1.308 1.404-2.138c.337-.83.503-1.74.503-2.741q.001-1.495-.503-2.741c-.342-.83-.805-1.544-1.404-2.138a6.3 6.3 0 0 0-2.102-1.388a6.9 6.9 0 0 0-2.62-.493m0-4.34q2.445-.001 4.527.85q2.083.846 3.602 2.334a10.7 10.7 0 0 1 2.379 3.51q.86 2.031.86 4.407t-.86 4.406a10.7 10.7 0 0 1-2.38 3.516c-1.01.991-2.213 1.766-3.6 2.334q-2.084.845-4.528.845q-2.445 0-4.527-.845c-1.388-.568-2.58-1.343-3.586-2.334a10.8 10.8 0 0 1-2.37-3.516q-.86-2.03-.86-4.406t.86-4.406a10.8 10.8 0 0 1 2.37-3.511a10.9 10.9 0 0 1 3.586-2.334q2.082-.851 4.527-.85M83.95 187.496c0-3.691 2.42-6.724 6.373-6.724c3.778 0 6.328 2.902 6.328 6.725s-2.55 6.72-6.328 6.72c-3.953 0-6.373-3.028-6.373-6.72m17.007 0v-10.502h-4.568v2.55c-1.453-1.891-3.646-3.078-6.634-3.078c-5.89 0-10.503 4.612-10.503 11.03c0 6.414 4.613 11.031 10.503 11.031c2.988 0 5.18-1.187 6.634-3.078V198h4.568zM75.207 198v-13.183c0-4.965-3.164-8.305-8.259-8.35c-2.681-.045-5.453.79-7.384 3.737c-1.449-2.329-3.737-3.737-6.946-3.737c-2.239 0-4.437.659-6.152 3.118v-2.59h-4.567V198h4.612v-11.644c0-3.647 2.022-5.583 5.14-5.583c3.034 0 4.573 1.976 4.573 5.538V198h4.613v-11.645c0-3.647 2.112-5.583 5.14-5.583c3.124 0 4.618 1.976 4.618 5.538V198z'/></svg>
        """
        , unsafe_allow_html=True)


if title == 'Yes':
    americanexpresscard_image()
else:
    vervecard_image()


st.write("The current movie title is", title)
    
