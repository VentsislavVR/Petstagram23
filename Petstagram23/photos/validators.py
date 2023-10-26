from django.core.exceptions import ValidationError

from Petstagram23.core.utils import megabytes_to_bytes

#
# def validate_file_size(image_object):
#     if image_object > 5242880:
#         raise ValidationError(
#             'The maximum file size that can be uploaded is 5MB'
#         )

def validate_file_less_than_5mb(fileobj):
    filesize = fileobj.file.size
    megabyte_limit = 5.0

    if filesize > megabytes_to_bytes(megabyte_limit):
        raise ValidationError(
            f'The maximum file size that can be uploaded is {megabyte_limit}MB'
        )