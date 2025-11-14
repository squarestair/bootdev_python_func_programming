def count_nested_levels(nested_documents, target_document_id, level=1):
    for document_id in nested_documents:
        if document_id == target_document_id:
            # print("LEVEL found",document_id)
            return level
        else:
            # print("else DOC ID: ",document_id, " ", nested_documents[document_id])
            a = count_nested_levels(nested_documents[document_id],target_document_id,level+1)
            if a != -1:
                return a
    return -1
