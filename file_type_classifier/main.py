class FileMask(object):
    def __init__(self, file_format: str, signature: str) -> None:
        self.file_format = file_format
        self.signature = signature
    
    def match(self, file_bytes_string: str) -> bool:
        return file_bytes_string.startswith(self.signature)

def file_bytes_reader(file_path: str) -> str:
    with open(file_path, 'rb') as file:
        file_content = file.read(1024)
        return file_content.hex(" ", 1).upper()
    
FILES_MASKS = [
    FileMask('#!',  '23 21') ,
    FileMask('pcap',  'D4 C3 B2 A1') ,
    FileMask('pcap',  '4D 3C B2 A1') ,
    FileMask('pcapng',  '0A 0D 0D 0A') ,
    FileMask('rpm',  'ED AB EE DB') ,
    FileMask('sqlite',  '53 51 4C 69 74 65 20 66 6F 72 6D 61 74 20 33 00') ,
    FileMask('bin',  '53 50 30 31') ,
    FileMask('wad',  '49 57 41 44') ,
    FileMask('PICPIFSEAYTR',  '00') ,
    FileMask('PDB',  '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00') ,
    FileMask('DBA',  'BE BA FE CA') ,
    FileMask('DBA',  '00 01 42 44') ,
    FileMask('TDA',  '00 01 44 54') ,
    FileMask('TDF$',  '54 44 46 24') ,
    FileMask('TDEF',  '54 44 45 46') ,
    FileMask('ico',  '00 00 01 00') ,
    FileMask('icns',  '69 63 6e 73') ,
    FileMask('3gp3g2',  '66 74 79 70 33 67') ,
    FileMask('ztar.z',  '1F 9D') ,
    FileMask('ztar.z',  '1F A0') ,
    FileMask('lzh',  '2D 68 6C 30 2D') ,
    FileMask('lzh',  '2D 68 6C 35 2D') ,
    FileMask('bac',  '42 41 43 4B 4D 49 4B 4544 49 53 4B') ,
    FileMask('idx',  '49 4E 44 58') ,
    FileMask('plist',  '62 70 6C 69 73 74') ,
    FileMask('bz2',  '42 5A 68') ,
    FileMask('gif',  '47 49 46 38 37 61') ,
    FileMask('gif',  'GIF87a') ,
    FileMask('tif',  '49 49 2A 00') ,
    FileMask('tiff',  '49 49 2A 00') ,
    FileMask('cr2',  '49 49 2A 00 10 00 00 0043 52') ,
    FileMask('cin',  '80 2A 5F D7') ,
    FileMask('nui',  '4E 55 52 55 49 4D 47') ,
    FileMask('nup',  '4E 55 52 55 49 4D 47') ,
    FileMask('dpx',  '53 44 50 58') ,
    FileMask('exr',  '76 2F 31 01') ,
    FileMask('bpg',  '42 50 47 FB') ,
    FileMask('jpeg',  'FF D8 FF DB') ,
    FileMask('jpg',  'FF D8 FF DB') ,
    FileMask('jpg',  'FF D8 FF E0') ,
    FileMask('jp2',  '00 00 00 0C 6A 50 20 20 0D 0A 87 0A') ,
    FileMask('lz',  '4C 5A 49 50') ,
    FileMask('cpio',  '30 37 30 37 30 37') ,
    FileMask('exe',  '4D 5A') ,
    FileMask('exe',  '5A 4D') ,
    FileMask('zip',  '50 4B 03 04') ,
    FileMask('zip',  '50 4B 07 08') ,
    FileMask('rar',  '52 61 72 21 1A 07 00') ,
    FileMask('rar',  '52 61 72 21 1A 07 01 00') ,
    FileMask('png',  '89 50 4E 47 0D 0A 1A 0A') ,
    FileMask('com',  'C9') ,
    FileMask('class',  'CA FE BA BE') ,
    FileMask('txt ',  'EF BB BF') ,
    FileMask('txt ',  'FF FE') ,
    FileMask('txt ',  'FE FF') ,
    FileMask('txt',  'FF FE 00 00') ,
    FileMask('txt ',  '0E FE FF') ,
    FileMask('ps',  '25 21 50 53') ,
    FileMask('eps',  '25 21 50 53 2D 41 64 6F 62 65 2D 33 2E 30 20 45 50 53 46 2D 33 2E 30') ,
    FileMask('eps',  '25 21 50 53 2D 41 64 6F 62 65 2D 33 2E 31 20 45 50 53 46 2D 33 2E 30') ,
    FileMask('chm',  '49 54 53 46 03 00 00 0060 00 00 00') ,
    FileMask('hlp',  '3F 5F') ,
    FileMask('pdf',  '25 50 44 46 2D') ,
    FileMask('asf',  '30 26 B2 75 8E 66 CF 11A6 D9 00 AA 00 62 CE 6C') ,
    FileMask('ogg',  '4F 67 67 53') ,
    FileMask('psd',  '38 42 50 53') ,
    FileMask('mp3',  'FF FB') ,
    FileMask('mp3',  'FF F2') ,
    FileMask('mp3',  'ÿó') ,
    FileMask('mp3',  '49 44 33') ,
    FileMask('bmp',  '42 4D') ,
    FileMask('iso',  '43 44 30 30 31') ,
    FileMask('cdi',  '43 44 30 30 31') ,
    FileMask('mgw',  '6D 61 69 6E 2E 62 73') ,
    FileMask('nes',  '4E 45 53') ,
    FileMask('d64',  'A0 32 41 A0 A0 A0') ,
    FileMask('g64',  '47 53 52 2D 31 35 34 31') ,
    FileMask('d81',  'A0 33 44 A0 A0') ,
    FileMask('t64',  '43 36 34 20 74 61 70 65 20 69 6D 61 67 65 20 66 69 6C 65') ,
    FileMask('crt',  '43 36 34 20 43 41 52 54 52 49 44 47 45 20 20 20') ,
    FileMask('fits',  '53 49 4D 50 4C 45 20 203D 20 20 20 20 20 20 2020 20 20 20 20 20 20 2020 20 20 20 20 54') ,
    FileMask('flac',  '66 4C 61 43') ,
    FileMask('mid',  '4D 54 68 64') ,
    FileMask('doc',  'D0 CF 11 E0 A1 B1 1A E1') ,
    FileMask('dex',  '64 65 78 0A 30 33 35 00') ,
    FileMask('vmdk',  '4B 44 4D') ,
    FileMask('vmdk',  '23 20 44 69 73 6B 20 44 65 73 63 72 69 70 74 6F') ,
    FileMask('crx',  '43 72 32 34') ,
    FileMask('fh8',  '41 47 44 33') ,
    FileMask('cwk',  '05 07 00 00 42 4F 42 4F05 07 00 00 00 00 00 0000 00 00 00 00 01') ,
    FileMask('cwk',  '06 07 E1 00 42 4F 42 4F06 07 E1 00 00 00 00 0000 00 00 00 00 01') ,
    FileMask('toast',  '45 52 02 00 00 00') ,
    FileMask('dmg',  '6B 6F 6C 79') ,
    FileMask('xar',  '78 61 72 21') ,
    FileMask('dat',  '50 4D 4F 43 43 4D 4F 43') ,
    FileMask('nes',  '4E 45 53 1A') ,
    FileMask('tar',  '75 73 74 61 72 00 30 30') ,
    FileMask('tox',  '74 6F 78 33') ,
    FileMask('MLV',  '4D 4C 56 49') ,
    FileMask('7z',  '37 7A BC AF 27 1C') ,
    FileMask('gz',  '1F 8B') ,
    FileMask('xz',  'FD 37 7A 58 5A 00') ,
    FileMask('lz4',  '04 22 4D 18') ,
    FileMask('cab',  '4D 53 43 46') ,
    FileMask('flif',  '46 4C 49 46') ,
    FileMask('mkv',  '1A 45 DF A3') ,
    FileMask('stg',  '4D 49 4C 20') ,
    FileMask('djvu',  '55') ,
    FileMask('djvu',  '4D') ,
    FileMask('der',  '30 82') ,
    FileMask('crt',  '2D 2D 2D 2D 2D 42 45 47 49 4E 20 43 45 52 54 49 46 49 43 41 54 45 2D 2D 2D 2D 2D') ,
    FileMask('csr',  '2D 2D 2D 2D 2D 42 45 47 49 4E 20 43 45 52 54 49 46 49 43 41 54 45 20 52 45 51 55 45 53 54 2D 2D 2D 2D 2D') ,
    FileMask('key',  '2D 2D 2D 2D 2D 42 45 47 49 4E 20 50 52 49 56 41 54 45 20 4B 45 59 2D 2D 2D 2D 2D') ,
    FileMask('key',  '2D 2D 2D 2D 2D 42 45 47 49 4E 20 44 53 41 20 50 52 49 56 41 54 45 20 4B 45 59 2D 2D 2D 2D 2D') ,
    FileMask('key',  '2D 2D 2D 2D 2D 42 45 47 49 4E 20 52 45 41 20 50 52 49 56 41 54 45 20 4B 45 59 2D 2D 2D 2D 2D') ,
    FileMask('ppk',  '50 75 54 54 59 2D 55 73 65 72 2D 4B 65 79 2D 46 69 6C 65 2D 32 3A') ,
    FileMask('ppk',  '50 75 54 54 59 2D 55 73 65 72 2D 4B 65 79 2D 46 69 6C 65 2D 33 3A') ,
    FileMask('pub',  '2D 2D 2D 2D 2D 42 45 47 49 4E 20 53 53 48 32 20 4B 45 59 2D 2D 2D 2D 2D') ,
    FileMask('dcm',  '44 49 43 4D') ,
    FileMask('woff',  '77 4F 46 46') ,
    FileMask('woff2',  '77 4F 46 32') ,
    FileMask('xml',  '3C 3F 78 6D 6C 20') ,
    FileMask('wasm',  '00 61 73 6D') ,
    FileMask('lep',  'CF 84 01') ,
    FileMask('swf',  '43 57 53') ,
    FileMask('deb',  '21 3C 61 72 63 68 3E 0A') ,
    FileMask('rtf',  '7B 5C 72 74 66 31') ,
    FileMask('tsv',  '47') ,
    FileMask('m2p',  '00 00 01 BA') ,
    FileMask('mpg',  '00 00 01 B3') ,
    FileMask('mp4',  '66 74 79 70 69 73 6F 6D') ,
    FileMask('zlib',  '78 01') ,
    FileMask('zlib',  '78 5E') ,
    FileMask('zlib',  '78 9C') ,
    FileMask('zlib',  '78 DA') ,
    FileMask('zlib',  '78 20') ,
    FileMask('zlib',  '78 7D') ,
    FileMask('zlib',  '78 BB') ,
    FileMask('zlib',  '78 F9') ,
    FileMask('lzfse',  '62 76 78 32') ,
    FileMask('orc',  '4F 52 43') ,
    FileMask('avro',  '4F 62 6A 01') ,
    FileMask('rc',  '53 45 51 36') ,
    FileMask('obt',  '65 87 78 56') ,
    FileMask('pcv',  '55 55 AA AA') ,
    FileMask('pbt',  '78 56 34') ,
    FileMask('ez2',  '45 4D 58 32') ,
    FileMask('ez3',  '45 4D 55 33') ,
    FileMask('luac',  '1B 4C 75 61') ,
    FileMask('alias',  '62 6F 6F 6B 00 00 00 006D 61 72 6B 00 00 00 00') ,
    FileMask('Identifier',  '5B 5A 6F 6E 65 54 72 616E 73 66 65 72 5D') ,
    FileMask('eml',  '52 65 63 65 69 76 65 643A') ,
    FileMask('tde',  '20 02 01 62 A0 1E AB 0702 00 00 00') ,
    FileMask('kdb',  '37 48 03 02 00 00 00 0058 35 30 39 4B 45 59') ,
    FileMask('zst',  '28 B5 2F FD') ,
    FileMask('rs',  '52 53 56 4B 44 41 54 41') ,
    FileMask('sml',  '3A 29 0A') ,
    FileMask('srt',  '31 0A 30 30') ,
    FileMask('vpk',  '34 12 AA 55') ,
    FileMask('ace',  '2A 2A 41 43 45 2A 2A') ,
    FileMask('arj',  '60 EA') ,
    FileMask('cab',  '49 53 63 28') ,
    FileMask('zoo',  '5A 4F 4F') ,
    FileMask('pbm',  '50 31 0A') ,
    FileMask('pbm',  '50 34 0A') ,
    FileMask('pgm',  '50 32 0A') ,
    FileMask('pgm',  '50 35 0A') ,
    FileMask('ppm',  '50 33 0A') ,
    FileMask('ppm',  '50 36 0A') ,
    FileMask('wmf',  'D7 CD C6 9A') ,
    FileMask('xcf',  '67 69 6D 70 20 78 63 66') ,
    FileMask('xpm',  '2F 2A 20 58 50 4D 20 2A2F') ,
    FileMask('aff',  '41 46 46') ,
    FileMask('Ex01',  '45 56 46 32') ,
    FileMask('e01',  '45 56 46') ,
    FileMask('qcow',  '51 46 49') ,
    FileMask('flv',  '46 4C 56') ,
    FileMask('vdi',  '3C 3C 3C 20 4F 72 61 636C 65 20 56 4D 20 56 6972 74 75 61 6C 42 6F 7820 44 69 73 6B 20 49 6D61 67 65 20 3E 3E 3E') ,
    FileMask('vhd',  '63 6F 6E 6E 65 63 74 6978') ,
    FileMask('vhdx',  '76 68 64 78 66 69 6C 65') ,
    FileMask('isz',  '49 73 5A 21') ,
    FileMask('daa',  '44 41 41') ,
    FileMask('evt',  '4C 66 4C 65') ,
    FileMask('evtx',  '45 6C 66 46 69 6C 65') ,
    FileMask('sdb',  '73 64 62 66') ,
    FileMask('grp',  '50 4D 43 43') ,
    FileMask('icm',  '4B 43 4D 53') ,
    FileMask('dat',  '72 65 67 66') ,
    FileMask('pst',  '21 42 44 4E') ,
    FileMask('drc',  '44 52 41 43 4F') ,
    FileMask('gribgrib2',  '47 52 49 42') ,
    FileMask('blend',  '42 4C 45 4E 44 45 52') ,
    FileMask('jxl',  '00 00 00 0C 4A 58 4C 20 0D 0A 87 0A') ,
    FileMask('ttf',  '00 01 00 00 00') ,
    FileMask('otf',  '4F 54 54 4F') ,
    FileMask('wim',  '4D 53 57 49 4D 00 00 00D0 00 00 00 00') ,
    FileMask('slob',  '21 2D 31 53 4C 4F 42 1F') ,
    FileMask('voc',  '43 72 65 61 74 69 76 65 20 56 6F 69 63 65 20 46 69 6C 65 1A 1A 00') ,
    FileMask('ausnd',  '2E 73 6E 64') ,
    FileMask('hazelrules',  '48 5a 4c 52 00 00 00 18') ,
    FileMask('flp',  '46 4C 68 64') ,
    FileMask('flm',  '31 30 4C 46') ,
    FileMask('mny',  '00 01 00 00 4D 53 49 53 41 4D 20 44 61 74 61 62 61 73 65') ,
    FileMask('accdb',  '00 01 00 00 53 74 61 6E 64 61 72 64 20 41 43 45 20 44 42') ,
    FileMask('mdb',  '00 01 00 00 53 74 61 6E 64 61 72 64 20 4A 65 74 20 44 42') ,
    FileMask('drw',  '01 FF 02 04 03 02') ,
    FileMask('dss',  '02 64 73 73') ,
    FileMask('dss',  '03 64 73 73') ,
    FileMask('adx',  '03 00 00 00 41 50 50 52') ,
    FileMask('indd',  '06 06 ED F5 D8 1D 46 E5 BD 31 EF E7 FE 74 B7 1D') ,
    FileMask('mxf',  '06 0E 2B 34 02 05 01 01 0D 01 02 01 01 02') ,
    FileMask('skf',  '07 53 4B 46') ,
    FileMask('dtd',  '07 64 74 32 64 64 74 64') ,
    FileMask('wallet',  '0A 16 6F 72 67 2E 62 69 74 63 6F 69 6E 2E 70 72') ,
    FileMask('doc',  '0D 44 4F 43') ,
    FileMask('nri',  '0E 4E 65 72 6F 49 53 4F') ,
    FileMask('wks',  '0E 57 4B 53') ,
    FileMask('sib',  '0F 53 49 42 45 4C 49 55 53') ,
    FileMask('dsp',  '23 20 4D 69 63 72 6F 73 6F 66 74 20 44 65 76 65 6C 6F 70 65 72 20 53 74 75 64 69 6F') ,
    FileMask('amr',  '23 21 41 4D 52') ,
    FileMask('sil',  '23 21 53 49 4C 4B 0A') ,
    FileMask('hdr',  '23 3F 52 41 44 49 41 4E 43 45 0A') ,
    FileMask('vbe',  '23 40 7E 5E') 
]

def file_type_classifier(file_path: str) -> str | None:
    file_data = file_bytes_reader(file_path)
    candidate_types = [file for file in FILES_MASKS if file.match(file_data)]

    if  not candidate_types:
        return None

    file_assignatures_lenght = [len(file.signature) for file in candidate_types]
    file_index = file_assignatures_lenght.index(max(file_assignatures_lenght))
    return candidate_types[file_index].file_format

def main() -> None:
    file_type = file_type_classifier('./res/image.png')
    print(file_type)

if __name__ == '__main__':
    main()
