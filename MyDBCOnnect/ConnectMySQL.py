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

# configuring time
from datetime import datetime
from datetime import date
from datetime import timedelta

today = date.today()
thisday = today.strftime('%A, %B %d %Y')

st.write('This script ran today, ' + thisday)

host = 'gewideas.com.ng'

st.write(host)

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
    <svg xmlns='http://www.w3.org/2000/svg' width='{card_width}' height='{card_height}' viewBox='0 0 256 199'><path d='M46.54 198.011V184.84c0-5.05-3.074-8.342-8.343-8.342c-2.634 0-5.488.878-7.464 3.732c-1.536-2.415-3.731-3.732-7.024-3.732c-2.196 0-4.39.658-6.147 3.073v-2.634h-4.61v21.074h4.61v-11.635c0-3.731 1.976-5.488 5.05-5.488c3.072 0 4.61 1.976 4.61 5.488v11.635h4.61v-11.635c0-3.731 2.194-5.488 5.048-5.488c3.074 0 4.61 1.976 4.61 5.488v11.635zm68.271-21.074h-7.463v-6.366h-4.61v6.366h-4.171v4.17h4.17v9.66c0 4.83 1.976 7.683 7.245 7.683c1.976 0 4.17-.658 5.708-1.536l-1.318-3.952c-1.317.878-2.853 1.098-3.951 1.098c-2.195 0-3.073-1.317-3.073-3.513v-9.44h7.463zm39.076-.44c-2.634 0-4.39 1.318-5.488 3.074v-2.634h-4.61v21.074h4.61v-11.854c0-3.512 1.536-5.488 4.39-5.488c.878 0 1.976.22 2.854.439l1.317-4.39c-.878-.22-2.195-.22-3.073-.22m-59.052 2.196c-2.196-1.537-5.269-2.195-8.562-2.195c-5.268 0-8.78 2.634-8.78 6.805c0 3.513 2.634 5.488 7.244 6.147l2.195.22c2.415.438 3.732 1.097 3.732 2.195c0 1.536-1.756 2.634-4.83 2.634s-5.488-1.098-7.025-2.195l-2.195 3.512c2.415 1.756 5.708 2.634 9 2.634c6.147 0 9.66-2.853 9.66-6.805c0-3.732-2.854-5.708-7.245-6.366l-2.195-.22c-1.976-.22-3.512-.658-3.512-1.975c0-1.537 1.536-2.415 3.951-2.415c2.635 0 5.269 1.097 6.586 1.756zm122.495-2.195c-2.635 0-4.391 1.317-5.489 3.073v-2.634h-4.61v21.074h4.61v-11.854c0-3.512 1.537-5.488 4.39-5.488c.879 0 1.977.22 2.855.439l1.317-4.39c-.878-.22-2.195-.22-3.073-.22m-58.833 10.976c0 6.366 4.39 10.976 11.196 10.976c3.073 0 5.268-.658 7.463-2.414l-2.195-3.732c-1.756 1.317-3.512 1.975-5.488 1.975c-3.732 0-6.366-2.634-6.366-6.805c0-3.951 2.634-6.586 6.366-6.805c1.976 0 3.732.658 5.488 1.976l2.195-3.732c-2.195-1.757-4.39-2.415-7.463-2.415c-6.806 0-11.196 4.61-11.196 10.976m42.588 0v-10.537h-4.61v2.634c-1.537-1.975-3.732-3.073-6.586-3.073c-5.927 0-10.537 4.61-10.537 10.976s4.61 10.976 10.537 10.976c3.073 0 5.269-1.097 6.586-3.073v2.634h4.61zm-16.904 0c0-3.732 2.415-6.805 6.366-6.805c3.732 0 6.367 2.854 6.367 6.805c0 3.732-2.635 6.805-6.367 6.805c-3.951-.22-6.366-3.073-6.366-6.805m-55.1-10.976c-6.147 0-10.538 4.39-10.538 10.976s4.39 10.976 10.757 10.976c3.073 0 6.147-.878 8.562-2.853l-2.196-3.293c-1.756 1.317-3.951 2.195-6.146 2.195c-2.854 0-5.708-1.317-6.367-5.05h15.587v-1.755c.22-6.806-3.732-11.196-9.66-11.196m0 3.951c2.853 0 4.83 1.757 5.268 5.05h-10.976c.439-2.854 2.415-5.05 5.708-5.05m114.372 7.025v-18.879h-4.61v10.976c-1.537-1.975-3.732-3.073-6.586-3.073c-5.927 0-10.537 4.61-10.537 10.976s4.61 10.976 10.537 10.976c3.074 0 5.269-1.097 6.586-3.073v2.634h4.61zm-16.903 0c0-3.732 2.414-6.805 6.366-6.805c3.732 0 6.366 2.854 6.366 6.805c0 3.732-2.634 6.805-6.366 6.805c-3.952-.22-6.366-3.073-6.366-6.805m-154.107 0v-10.537h-4.61v2.634c-1.537-1.975-3.732-3.073-6.586-3.073c-5.927 0-10.537 4.61-10.537 10.976s4.61 10.976 10.537 10.976c3.074 0 5.269-1.097 6.586-3.073v2.634h4.61zm-17.123 0c0-3.732 2.415-6.805 6.366-6.805c3.732 0 6.367 2.854 6.367 6.805c0 3.732-2.635 6.805-6.367 6.805c-3.951-.22-6.366-3.073-6.366-6.805'/><path fill='#ff5f00' d='M93.298 16.903h69.15v124.251h-69.15z'/><path fill='#eb001b' d='M97.689 79.029c0-25.245 11.854-47.637 30.074-62.126C114.373 6.366 97.47 0 79.03 0C35.343 0 0 35.343 0 79.029s35.343 79.029 79.029 79.029c18.44 0 35.343-6.366 48.734-16.904c-18.22-14.269-30.074-36.88-30.074-62.125'/><path fill='#f79e1b' d='M255.746 79.029c0 43.685-35.343 79.029-79.029 79.029c-18.44 0-35.343-6.366-48.734-16.904c18.44-14.488 30.075-36.88 30.075-62.125s-11.855-47.637-30.075-62.126C141.373 6.366 158.277 0 176.717 0c43.686 0 79.03 35.563 79.03 79.029'/></svg>
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


def americanexpress_image():
    americanexpress = st.markdown(
        f"""
        <svg xmlns='http://www.w3.org/2000/svg' width='{card_width}' height='{card_height}' viewBox='0 0 24 24'><path fill='#016FD0' d='M16.015 14.378c0-.32-.135-.496-.344-.622c-.21-.12-.464-.135-.81-.135h-1.543v2.82h.675v-1.027h.72c.24 0 .39.024.478.125c.12.13.104.38.104.55v.35h.66v-.555c-.002-.25-.017-.376-.108-.516a.75.75 0 0 0-.33-.234l.02-.008a.78.78 0 0 0 .48-.747zm-.87.407l-.028-.002c-.09.053-.195.058-.33.058h-.81v-.63h.824c.12 0 .24 0 .33.05a.27.27 0 0 1 .15.255c0 .12-.045.215-.134.27zm5.152 1.052H19v.6h1.304c.676 0 1.05-.278 1.05-.884c0-.28-.066-.448-.187-.582c-.153-.133-.392-.193-.73-.207l-.376-.015c-.104 0-.18 0-.255-.03a.21.21 0 0 1-.15-.21c0-.09.017-.166.09-.21a.5.5 0 0 1 .272-.06h1.23v-.602h-1.35c-.704 0-.958.437-.958.84c0 .9.776.855 1.407.87c.104 0 .18.015.225.06c.046.03.082.106.082.18c0 .077-.035.15-.08.18c-.06.053-.15.07-.277.07M0 0v10.096L.81 8.22h1.75l.225.464V8.22h2.043l.45 1.02l.437-1.013h6.502c.295 0 .56.057.756.236v-.23h1.787v.23c.307-.17.686-.23 1.12-.23h2.606l.24.466v-.466h1.918l.254.465v-.466h1.858v3.948H20.87l-.36-.6v.585h-2.353l-.256-.63h-.583l-.27.614h-1.213c-.48 0-.84-.104-1.08-.24v.24h-2.89v-.884c0-.12-.03-.12-.105-.135h-.105v1.036H6.067v-.48l-.21.48H4.69l-.202-.48v.465H2.235l-.256-.624H1.4l-.256.624H0V24h23.786v-7.108c-.27.135-.613.18-.973.18H21.09v-.255c-.21.165-.57.255-.914.255H14.71v-.9c0-.12-.018-.12-.12-.12h-.075v1.022h-1.8v-1.066c-.298.136-.643.15-.928.136h-.214v.915h-2.18l-.54-.617l-.57.6H4.742v-3.93h3.61l.518.602l.554-.6h2.412c.28 0 .74.03.942.225v-.24h2.177c.202 0 .644.045.903.225v-.24h3.265v.24c.163-.164.508-.24.803-.24h1.89v.24c.194-.15.464-.24.84-.24h1.176V0zm21.156 14.955l.01.016c.01.01.024.01.032.02zm2.672-1.873h.065v.555h-.065zm.037 1.948v-.005c-.03-.025-.046-.048-.075-.07c-.15-.153-.39-.215-.764-.225l-.36-.012a.9.9 0 0 1-.27-.03a.21.21 0 0 1-.15-.21q0-.136.09-.204c.076-.045.15-.05.27-.05h1.223v-.588h-1.283c-.69 0-.96.437-.96.84c0 .9.78.855 1.41.87c.104 0 .18.015.224.06c.046.03.076.106.076.18c0 .07-.034.138-.09.18c-.045.056-.136.07-.27.07h-1.288v.605h1.287c.42 0 .734-.118.9-.36h.03c.09-.134.135-.3.135-.523c0-.24-.045-.39-.135-.526zm-5.268-.822v-.583h-2.235v2.833h2.235v-.585h-1.57v-.57h1.533v-.584h-1.532v-.51M13.51 8.787h.685V11.6h-.684zm-.384.756l-.007.006c0-.314-.13-.5-.34-.624c-.217-.125-.47-.135-.81-.135H10.43v2.82h.674v-1.034h.72c.24 0 .39.03.487.12c.122.136.107.378.107.548v.354h.677v-.553c0-.25-.016-.375-.11-.516a.8.8 0 0 0-.33-.237c.172-.07.472-.3.472-.75zm-.855.396h-.015c-.09.054-.195.056-.33.056H11.1v-.623h.825c.12 0 .24.004.33.05c.09.04.15.128.15.25s-.047.22-.134.266zm3.649-.566h.632v-.6h-.644c-.464 0-.804.105-1.02.33c-.286.3-.362.69-.362 1.11c0 .512.123.833.36 1.074c.232.238.645.31.97.31h.78l.255-.627h1.39l.262.627h1.36v-2.11l1.272 2.11h.95l.002.002V8.786h-.684v1.963l-1.18-1.96h-1.02V11.4L18.11 8.744h-1.004l-.943 2.22h-.3c-.177 0-.362-.03-.468-.134c-.125-.15-.186-.36-.186-.662c0-.285.08-.51.194-.63c.133-.135.272-.165.516-.165zm1.668-.108l.464 1.118v.002h-.93zM2.38 10.97l.254.628H4V9.393l.972 2.205h.584l.973-2.202l.015 2.202h.69v-2.81H6.118l-.807 1.904l-.876-1.905H3.343v2.663L2.205 8.787h-.997L.01 11.597h.72l.26-.626zm-.688-1.705l.46 1.118l-.003.002h-.915l.457-1.12zm10.164 4.355H9.714l-.85.923l-.825-.922H5.346v2.82H8l.855-.932l.824.93h1.302v-.94h.838c.6 0 1.17-.164 1.17-.945l-.006-.003c0-.78-.598-.93-1.128-.93zM7.67 15.853l-.014-.002H6.02v-.557h1.47v-.574H6.02v-.51H7.7l.733.82l-.764.824zm2.642.33l-1.03-1.147l1.03-1.108v2.253zm1.553-1.258h-.885v-.717h.885c.24 0 .42.098.42.344c0 .243-.15.372-.42.372zM9.967 9.373v-.586H7.73V11.6h2.237v-.58H8.4v-.564h1.527V9.88H8.4v-.507'/></svg>
        """
        , unsafe_allow_html=True)

def verve_image():
    verve = st.markdown(
        f"""
        <svg viewBox='0 -227 750 750' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' fill='#000000' stroke='#000000'><g id='SVGRepo_bgCarrier' stroke-width='0'></g><g id='SVGRepo_tracerCarrier' stroke-linecap='round' stroke-linejoin='round'></g><g id='SVGRepo_iconCarrier'> <desc>Created with Sketch.</desc> <defs> </defs> <g id='Page-1' stroke='none' stroke-width='1' fill='none' fill-rule='evenodd'> <g id='verve' fill-rule='nonzero'> <rect id='Rectangle-path' fill='#00425F' x='0' y='0' width='{card_width}' height='{card_height}' rx='20'> </rect> <g id='Group' transform='translate(66.000000, 35.000000)'> <circle id='Oval' fill='#EE312A' cx='107.5' cy='107.5' r='107.5'> </circle> <path d='M107.499995,153.362725 C83.4681523,98.8873337 65.8448492,48 65.8448492,48 L29,48 C29,48 51.4257509,113.317063 93.080897,195 L121.919103,195 C163.574249,113.317063 186,48 186,48 L149.155141,48 C149.155141,48 131.531838,98.8873337 107.499995,153.362725 Z' id='Shape' fill='#FFFFFF'> </path> <path d='M621.113436,146.540569 L549.314677,146.540569 C549.314677,146.540569 550.909818,170.666883 582.820685,170.666883 C598.775608,170.666883 614.731728,165.837988 614.731728,165.837988 L617.923246,191.567306 C617.923246,191.567306 601.967125,198 579.629297,198 C547.719572,198 519,181.918591 519,136.891995 C519,101.513298 541.3365,79 573.247544,79 C621.113436,79 624.304953,127.243281 621.113436,146.540569 Z M571.652504,101.513298 C550.909771,101.513298 549.314677,124.026597 549.314677,124.026597 L593.989005,124.026597 C593.989005,124.026597 592.39391,101.513298 571.652504,101.513298 Z' id='Shape' fill='#FFFFFF'> </path> <path d='M373.214385,108.623324 L378,83.0294396 C378,83.0294396 341.041315,71.783453 311,92.627117 L311,195 L342.906457,195 L342.903941,111.822332 C355.665024,102.224785 373.214385,108.623324 373.214385,108.623324 Z' id='Shape' fill='#FFFFFF'> </path> <path d='M286.113913,146.540569 L214.315713,146.540569 C214.315713,146.540569 215.910841,170.666883 247.82146,170.666883 C263.776259,170.666883 279.730937,165.837988 279.730937,165.837988 L282.922429,191.567306 C282.922429,191.567306 266.967761,198 244.630107,198 C212.719312,198 184,181.918591 184,136.891995 C184,101.513298 206.337654,79 238.248449,79 C286.113913,79 289.30405,127.243281 286.113913,146.540569 Z M236.652039,101.513298 C215.910795,101.513298 214.315713,124.026597 214.315713,124.026597 L258.989693,124.026597 C258.989693,124.026597 257.394601,101.513298 236.652039,101.513298 Z' id='Shape' fill='#FFFFFF'> </path> <path d='M451,156.605781 C441.05272,132.406506 433.027561,107.460679 426.999064,82 L395,82.0042285 C395,82.0042285 411.000193,143.797279 438.202963,195 L463.797037,195 C490.999826,143.797279 507,82.0156194 507,82.0156194 L475.000936,82.0156194 C468.971104,107.470841 460.945967,132.411374 451,156.605781 Z' id='Shape' fill='#FFFFFF'> </path> </g> </g> </g> </g></svg>
        """
        , unsafe_allow_html=True)


if title == 'Yes':
    mastercard_image()
else:
    verve_image()


st.write("The current movie title is", title)
    
