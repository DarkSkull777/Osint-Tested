import marshal

enc = b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\xf3 \x03\x00\x00\x97\x00d\x00d\x01l\x00Z\x00d\x00d\x01l\x01Z\x01d\x00d\x01l\x02Z\x02\x02\x00e\x02j\x03\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x03Z\x04\x02\x00e\x05e\x04\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x04Z\x06\x02\x00e\x07d\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00Z\x08\x02\x00e\x00j\t\x00\x00\x00\x00\x00\x00\x00\x00d\x06e\x06\x9b\x00d\x07e\x08\x9b\x00\x9d\x04\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00Z\ne\n\xa0\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00Z\x0c\x02\x00e\x05d\x08\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x05d\te\x0cd\n\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x05d\x0be\x0cd\x0c\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x05d\re\x0cd\x0e\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x05d\x0fe\x0cd\x10\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x05d\x11e\x0cd\x12\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x05d\x13e\x0cd\x0e\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x05d\x14e\x0cd\x0c\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x15e\x0cv\x00r\x14\x02\x00e\x05d\x16e\x0cd\x15\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x05d\x17e\x0cd\x18\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x05d\x19e\x0cd\x10\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x05d\x1ae\x0cd\x0e\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x05d\x1be\x0cd\x1c\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x05d\x17e\x0cd\x18\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x05d\x1d\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x01j\r\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00)\x1e\xe9\x00\x00\x00\x00N\xda\x05cleara \x02\x00\x00\n      ::::::::   :::::::: ::::::::::: ::::    ::: ::::::::::: \n    :+:    :+: :+:    :+:    :+:     :+:+:   :+:     :+:   \n   +:+    +:+ +:+           +:+     :+:+:+  +:+     +:+   \n  +#+    +:+ +#++:++#++    +#+     +#+ +:+ +#+     +#+  \n +#+    +#+        +#+    +#+     +#+  +#+#+#     +#+  Number\n#+#    #+# #+#    #+#    #+#     #+#   #+#+#     #+# ~ Scanner\n########   ######## ########### ###    ####     ###  v1.5\n\n  Coded by : Dymles Ganz\n  Github   : https://github.com/DarkSkull777/Osint-Tested\n  Contact  : https://t.me/DymlesCode\n\xda 58e71efe7992866366012249b47430b6z\x1eMasukkan nomor telepon (+62): z,http://apilayer.net/api/validate?access_key=z\x08&number=z\x10Hasil Pencarian:z\x04ID: \xda\x05validz\x06Name: \xda\x0clocal_formatz\x07Score: \xda\tline_typez\x08Access: \xda\x07carrierz\x14Phones E164 format: \xda\x14international_formatz\x0cNumberType: z\x10NationalFormat: \xda\rdialling_codez\rDialingCode: z\rCountryCode: \xda\x0ccountry_codez\tCarrier: z\x06Type: z\tAddress: \xda\x08locationz!Berhasil Menemukan beberapa data!)\x0e\xda\x08requests\xda\x03sys\xda\x02os\xda\x06system\xda\tascii_art\xda\x05print\xda\x07api_key\xda\x05input\xda\x0cphone_number\xda\x03get\xda\x08response\xda\x04json\xda\x04data\xda\x04exit\xa9\x00\xf3\x00\x00\x00\x00\xda\x06Dymles\xfa\x08<module>r\x1e\x00\x00\x00\x01\x00\x00\x00sX\x02\x00\x00\xf0\x03\x01\x01\x01\xd8\x00\x0f\x80\x0f\x80\x0f\x80\x0f\xd8\x00\n\x80\n\x80\n\x80\n\xd8\x00\t\x80\t\x80\t\x80\t\xf0\x06\x00\x01\n\x80\x02\x84\t\x88\'\xd1\x00\x12\xd4\x00\x12\xd0\x00\x12\xf0\x08\x0c\r\x04\x80\t\xf0\x1c\x00\x01\x06\x80\x05\x80i\xd1\x00\x10\xd4\x00\x10\xd0\x00\x10\xe0\n,\x80\x07\xd8\x0f\x14\x88u\xd0\x155\xd1\x0f6\xd4\x0f6\x80\x0c\xe0\x0b\x17\x888\x8c<\xd0\x18f\xc0w\xd0\x18f\xd0\x18f\xd0Xd\xd0\x18f\xd0\x18f\xd1\x0bg\xd4\x0bg\x80\x08\xe0\x07\x0f\x87}\x82}\x81\x7f\x84\x7f\x80\x04\xe0\x00\x05\x80\x05\xd0\x06\x18\xd1\x00\x19\xd4\x00\x19\xd0\x00\x19\xd8\x00\x05\x80\x05\xd0\x06\x1c\x88T\x90\'\x8c]\xd0\x06\x1c\xd0\x06\x1c\xd1\x00\x1d\xd4\x00\x1d\xd0\x00\x1d\xd8\x00\x05\x80\x05\xd0\x06%\x88t\x90N\xd4\x0f#\xd0\x06%\xd0\x06%\xd1\x00&\xd4\x00&\xd0\x00&\xd8\x00\x05\x80\x05\xd0\x06#\x90\x04\x90[\xd4\x10!\xd0\x06#\xd0\x06#\xd1\x00$\xd4\x00$\xd0\x00$\xd8\x00\x05\x80\x05\xd0\x06"\x90\x14\x90i\x94\x1f\xd0\x06"\xd0\x06"\xd1\x00#\xd4\x00#\xd0\x00#\xd8\x00\x05\x80\x05\xd0\x06;\x98T\xd0"8\xd4\x1d9\xd0\x06;\xd0\x06;\xd1\x00<\xd4\x00<\xd0\x00<\xd8\x00\x05\x80\x05\xd0\x06(\x90T\x98+\xd4\x15&\xd0\x06(\xd0\x06(\xd1\x00)\xd4\x00)\xd0\x00)\xd8\x00\x05\x80\x05\xd0\x06/\x98\x14\x98n\xd4\x19-\xd0\x06/\xd0\x06/\xd1\x000\xd4\x000\xd0\x000\xf0\x06\x00\x04\x13\x90d\xd0\x03\x1a\xd0\x03\x1a\xd8\x04\t\x80E\xd0\n1\x98$\x98\x7f\xd4\x1a/\xd0\n1\xd0\n1\xd1\x042\xd4\x042\xd0\x042\xe0\x00\x05\x80\x05\xd0\x06,\x90d\x98>\xd4\x16*\xd0\x06,\xd0\x06,\xd1\x00-\xd4\x00-\xd0\x00-\xd8\x00\x05\x80\x05\xd0\x06#\x90$\x90y\x94/\xd0\x06#\xd0\x06#\xd1\x00$\xd4\x00$\xd0\x00$\xd8\x00\x05\x80\x05\xd0\x06"\x88t\x90K\xd4\x0f \xd0\x06"\xd0\x06"\xd1\x00#\xd4\x00#\xd0\x00#\xd8\x00\x05\x80\x05\xd0\x06$\x90$\x90z\xd4\x12"\xd0\x06$\xd0\x06$\xd1\x00%\xd4\x00%\xd0\x00%\xd8\x00\x05\x80\x05\xd0\x06,\x90d\x98>\xd4\x16*\xd0\x06,\xd0\x06,\xd1\x00-\xd4\x00-\xd0\x00-\xf0\x06\x00\x01\x06\x80\x05\xd0\x06)\xd1\x00*\xd4\x00*\xd0\x00*\xd8\x00\x08\x80\x03\x84\x08\x81\n\x84\n\x80\n\x80\n\x80\nr\x1c\x00\x00\x00'

exec(marshal.loads(enc))
